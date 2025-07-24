# Detectores de Borda com OpenCV

Este projeto em Python demonstra e compara três algoritmos clássicos de detecção de bordas em imagens: **Canny**, **Sobel** e **Prewitt**. Utilizando as bibliotecas OpenCV e Matplotlib, o script aplica cada um desses filtros a uma imagem de entrada e exibe os resultados lado a lado para uma fácil avaliação visual.

## O que é Detecção de Borda?

A detecção de borda é uma técnica fundamental em processamento de imagens e visão computacional. Seu objetivo é identificar pontos em uma imagem onde a luminosidade ou intensidade da cor muda bruscamente. Essas mudanças geralmente correspondem a bordas de objetos, sendo cruciais para tarefas como reconhecimento de objetos, segmentação de imagens e extração de características.

## Algoritmos Implementados

O script implementa e compara os seguintes detectores:

### 1. Detector de Canny
-   **Descrição**: É um dos detectores de borda mais eficazes e amplamente utilizados. Trata-se de um algoritmo multi-estágio que envolve:
    1.  Redução de ruído com um filtro Gaussiano.
    2.  Cálculo do gradiente de intensidade da imagem.
    3.  Supressão de não-máximos para afinar as bordas.
    4.  Limiarização dupla (hysteresis) para filtrar bordas fracas.
-   **Implementação**: Utiliza a função otimizada `cv2.Canny()` do OpenCV.

### 2. Filtro de Sobel
-   **Descrição**: É um operador baseado em gradiente que calcula a derivada de primeira ordem da imagem em ambas as direções horizontal (X) e vertical (Y). As bordas são detectadas onde o gradiente é máximo.
-   **Implementação**: Usa a função `cv2.Sobel()` para calcular os gradientes X e Y, que são então combinados pela função `cv2.magnitude()` para gerar o mapa de bordas final.

### 3. Filtro de Prewitt
-   **Descrição**: Similar ao Sobel, o Prewitt também é um operador baseado em gradiente. Ele utiliza uma máscara (kernel) ligeiramente diferente, que é mais simples mas pode ser mais sensível a ruído.
-   **Implementação**: Este filtro é implementado manualmente no script, definindo-se explicitamente os kernels Prewitt para as direções X e Y e aplicando-os à imagem através da convolução com a função `cv2.filter2D()`. Isso demonstra o princípio fundamental por trás dos filtros de gradiente.

## Estrutura do Código

1.  **`exibir_imagens()`**: Uma função auxiliar que usa Matplotlib para plotar múltiplas imagens em uma única figura, facilitando a comparação.
2.  **Carregamento da Imagem**: Carrega uma imagem de entrada (ex: `th.jpeg`) diretamente em escala de cinza.
3.  **Aplicação dos Filtros**: Cada um dos três algoritmos é aplicado sequencialmente à imagem original.
4.  **Exibição dos Resultados**: A função `exibir_imagens()` é chamada no final para mostrar a imagem original ao lado dos três mapas de bordas gerados.

## Dependências

Para executar este script, você precisará das seguintes bibliotecas:

-   `opencv-python`
-   `numpy`
-   `matplotlib`

Você pode instalar todas elas com um único comando via `pip`:
`
pip install opencv-python numpy matplotlib`

##Como Usar
Salve o código como detectoresborda.py.

Coloque uma imagem de sua escolha no mesmo diretório e nomeie-a como th.jpeg, ou altere o nome do arquivo diretamente no código.

Execute o script a partir do seu terminal:

`python detectoresborda.py`
Uma janela do Matplotlib será aberta, exibindo quatro painéis: a imagem original, o resultado do detector de Canny, o resultado do filtro de Sobel e o resultado do filtro de Prewitt.
`
Estrutura dos Arquivos
/seu-projeto
|
|-- detectoresborda.py      # O script principal
|-- th.jpeg                 # Imagem de exemplo para análise`
