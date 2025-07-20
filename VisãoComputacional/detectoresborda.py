import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para exibir as imagens lado a lado
def exibir_imagens(imgs, titulos, cmap='gray'):
    fig, axs = plt.subplots(1, len(imgs), figsize=(15, 5))
    for i, ax in enumerate(axs):
        ax.imshow(imgs[i], cmap=cmap)
        ax.set_title(titulos[i])
        ax.axis('off')
    plt.show()

# Carregando a imagem e convertendo para escala de cinza
imagem = cv2.imread("th.jpeg", cv2.IMREAD_GRAYSCALE)

# Verifica se a imagem foi carregada corretamente
if imagem is None:
    raise ValueError("Imagem não encontrada. Verifique o caminho do arquivo.")

# Detector de Canny
bordas_canny = cv2.Canny(imagem, threshold1=100, threshold2=200)

# Filtro de Sobel
sobelx = cv2.Sobel(imagem, cv2.CV_32F, 1, 0, ksize=3)  # Gradiente em X, convertido para float32
sobely = cv2.Sobel(imagem, cv2.CV_32F, 0, 1, ksize=3)  # Gradiente em Y, convertido para float32
sobel_total = cv2.magnitude(sobelx, sobely)

# Filtro de Prewitt - definindo as máscaras e convertendo para float32
prewitt_kernelx = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]], dtype=np.float32)
prewitt_kernely = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)

# Aplicando convolução com as máscaras Prewitt
prewittx = cv2.filter2D(imagem, cv2.CV_32F, prewitt_kernelx)
prewitty = cv2.filter2D(imagem, cv2.CV_32F, prewitt_kernely)

# Verificação de tamanhos e tipos
print("Tipo de prewittx:", prewittx.dtype, "Tamanho de prewittx:", prewittx.shape)
print("Tipo de prewitty:", prewitty.dtype, "Tamanho de prewitty:", prewitty.shape)

# Assegurando que os dois estão no tipo float32
if prewittx.dtype != np.float32:
    prewittx = prewittx.astype(np.float32)
if prewitty.dtype != np.float32:
    prewitty = prewitty.astype(np.float32)

# Redimensionando se necessário para garantir tamanhos iguais
if prewittx.shape != prewitty.shape:
    prewitty = cv2.resize(prewitty, (prewittx.shape[1], prewittx.shape[0]))

# Calculando a magnitude para o filtro de Prewitt
prewitt_total = cv2.magnitude(prewittx, prewitty)

# Exibindo as imagens lado a lado para comparação
exibir_imagens(
    [imagem, bordas_canny, sobel_total, prewitt_total],
    ["Imagem Original", "Detector de Canny", "Detector de Sobel", "Detector de Prewitt"]
)
