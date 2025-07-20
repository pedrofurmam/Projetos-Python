import cv2
import numpy as np
from matplotlib import pyplot as plt

# Função para plotar histogramas
def plot_histogram(image, ax, title):
    ax.hist(image.ravel(), 256, [0, 256])
    ax.set_title(title)

# Carregar a imagem em escala de cinza
imagem = cv2.imread('imagem4.jpg', cv2.IMREAD_GRAYSCALE)

# Aplicar equalização de histograma
imagem_equalizada = cv2.equalizeHist(imagem)

# Criar o negativo da imagem
imagem_negativa = cv2.bitwise_not(imagem)

# Configurar a plotagem das imagens e histogramas
fig, axs = plt.subplots(3, 2, figsize=(12, 8))

# Mostrar a imagem original
axs[0, 0].imshow(imagem, cmap='gray')
axs[0, 0].set_title('Imagem Original')
axs[0, 0].axis('off')  # Ocultar os eixos

# Mostrar o histograma da imagem original
plot_histogram(imagem, axs[0, 1], 'Histograma Original')

# Mostrar a imagem equalizada
axs[1, 0].imshow(imagem_equalizada, cmap='gray')
axs[1, 0].set_title('Imagem Equalizada')
axs[1, 0].axis('off')

# Mostrar o histograma da imagem equalizada
plot_histogram(imagem_equalizada, axs[1, 1], 'Histograma Equalizado')

# Mostrar a imagem negativa
axs[2, 0].imshow(imagem_negativa, cmap='gray')
axs[2, 0].set_title('Imagem Negativa')
axs[2, 0].axis('off')

# Mostrar o histograma da imagem negativa
plot_histogram(imagem_negativa, axs[2, 1], 'Histograma Negativo')

# Ajustar o layout
plt.tight_layout()
plt.show()
