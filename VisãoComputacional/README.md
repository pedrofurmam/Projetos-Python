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

## Como Usar

1.  Salve o código como `detectoresborda.py`.
2.  Coloque uma imagem de sua escolha no mesmo diretório e nomeie-a como `th.jpeg`, ou altere o nome do arquivo diretamente no código.
3.  Execute o script a partir do seu terminal:
    ```bash
    python detectoresborda.py
    ```
4.  Uma janela do Matplotlib será aberta, exibindo quatro painéis: a imagem original, o resultado do detector de Canny, o resultado do filtro de Sobel e o resultado do filtro de Prewitt.
   


# Detector de Veículos com Haar Cascade em OpenCV

Este projeto é uma implementação em Python que utiliza a biblioteca OpenCV para detectar veículos (carros) em uma imagem estática. Ele emprega um classificador Haar Cascade pré-treinado e inclui uma etapa de pós-processamento de Supressão de Não-Máximos (Non-Maximum Suppression) para refinar os resultados e evitar detecções duplicadas.

## Como Funciona

O script segue um pipeline de processamento de imagem bem definido para identificar os veículos:

1.  **Carregamento do Classificador**: Primeiramente, o script carrega um modelo pré-treinado, o `cars.xml`. Este arquivo contém as características (features) de Haar que o algoritmo usa para identificar objetos que se parecem com carros.

2.  **Pré-processamento da Imagem**: Para melhorar a precisão da detecção, a imagem de entrada passa por várias etapas de preparação:
    * **Conversão para Escala de Cinza**: A detecção de Haar Cascade opera em imagens de um único canal.
    * **Equalização de Histograma**: A função `cv2.equalizeHist` é aplicada para aumentar o contraste da imagem, o que ajuda a destacar as características dos veículos em diferentes condições de iluminação.
    * **Desfoque Gaussiano**: Um leve desfoque (`cv2.GaussianBlur`) é usado para reduzir o ruído da imagem, evitando falsos positivos.

3.  **Detecção Multi-escala Aprimorada**:
    * A função principal `cv2.detectMultiScale` é executada em um laço com diferentes parâmetros (`scaleFactor` e `minNeighbors`). Esta abordagem aumenta a robustez do detector, permitindo que ele encontre veículos de tamanhos variados e com diferentes níveis de confiança, melhorando a taxa de detecção geral.

4.  **Supressão de Não-Máximos (Non-Maximum Suppression - NMS)**:
    * A detecção inicial pode gerar múltiplos retângulos sobrepostos para um mesmo veículo. A função `non_max_suppression` implementada no script serve como um passo de pós-processamento crucial.
    * Ela analisa todos os retângulos detectados e remove os redundantes, mantendo apenas o que melhor representa cada veículo, com base em um limiar de sobreposição (IoU - Intersection over Union).

5.  **Visualização e Saída**:
    * Após a filtragem, o script desenha retângulos verdes na imagem colorida original ao redor de cada veículo unicamente detectado.
    * O resultado final é exibido em uma janela e também salvo como um novo arquivo de imagem.

## Dependências

Para executar este projeto, você precisa:

-   **Bibliotecas Python**:
    -   `opencv-python`
    -   `numpy`
-   **Arquivo do Classificador**:
    -   `cars.xml`: O arquivo Haar Cascade para detecção de carros. Você pode encontrá-lo no [repositório oficial do OpenCV](https://github.com/opencv/opencv/tree/master/data/haarcascades).

## Como Usar

1.  **Preparar o Ambiente**:
    * Salve o código como `detectorveiculos.py`.
    * Faça o download do arquivo `cars.xml` e coloque-o em um local acessível.
    * Tenha uma imagem com veículos para testar (ex: `imagem1.jpg`).

2.  **Instalar Dependências**:
    * Instale as bibliotecas necessárias via pip:
        ```bash
        pip install opencv-python numpy
        ```

3.  **Configurar os Caminhos no Código**:
    * **Importante**: O script utiliza caminhos de arquivo absolutos (hardcoded). Você **precisa** editar o código e alterar os seguintes caminhos para os locais corretos em seu computador:
        * A linha `car_cascade = cv2.CascadeClassifier(...)` deve apontar para onde você salvou o arquivo `cars.xml`.
        * A chamada da função `detect_vehicles(...)` no final do arquivo deve conter o caminho para a sua imagem de entrada e o caminho onde você deseja salvar a imagem de saída.

4.  **Executar o Script**:
    * Abra um terminal e execute o script:
        ```bash
        python detectorveiculos.py
        ```
5.  **Verificar o Resultado**:
    * O script imprimirá o número de veículos detectados no console.
    * Uma janela do OpenCV aparecerá mostrando a imagem com os veículos demarcados.
    * A imagem com o resultado será salva no caminho de saída especificado.
      
# Análise de Histogramas de Imagens com OpenCV e Matplotlib

Este projeto em Python demonstra o cálculo e a visualização de histogramas para imagens em escala de cinza. O script aplica duas transformações comuns — **Equalização de Histograma** e **Negativo de Imagem** — e exibe os resultados visuais e seus respectivos histogramas lado a lado para uma análise comparativa clara.

## O que é um Histograma de Imagem?

Um histograma é um gráfico que representa a distribuição da frequência das intensidades de pixels em uma imagem. Para uma imagem em escala de cinza de 8 bits, o eixo X do histograma vai de 0 (preto puro) a 255 (branco puro), enquanto o eixo Y mostra quantos pixels na imagem possuem cada um desses valores de intensidade.

A análise de histogramas é fundamental para entender as características de uma imagem, como brilho, contraste e a distribuição tonal geral.

## Conceitos e Transformações Aplicadas

O script explora os seguintes conceitos:

1.  **Histograma Original**: Mostra a distribuição de pixels da imagem como ela é. Uma imagem escura terá um histograma concentrado à esquerda, uma imagem clara terá um histograma concentrado à direita, e uma imagem de baixo contraste terá um histograma concentrado em uma faixa estreita.

2.  **Equalização de Histograma (`cv2.equalizeHist`)**:
    * **Objetivo**: Melhorar o contraste de uma imagem.
    * **Como funciona**: É uma técnica que redistribui as intensidades dos pixels para que a distribuição seja o mais uniforme e espalhada possível. Na prática, isso "alarga" as faixas de intensidade mais comuns, resultando em um maior contraste global e na revelação de detalhes que antes estavam obscurecidos. O histograma resultante tende a ser mais plano e a ocupar toda a faixa de 0 a 255.

3.  **Negativo de Imagem (`cv2.bitwise_not`)**:
    * **Objetivo**: Inverter as intensidades da imagem.
    * **Como funciona**: Cada valor de pixel `p` é transformado em `255 - p`. Isso transforma pixels pretos em brancos, brancos em pretos e inverte todos os tons de cinza. O histograma da imagem negativa é um "espelho" horizontal do histograma original.

## Estrutura do Código

-   **`plot_histogram()`**: Uma função auxiliar que recebe uma imagem e um eixo de plotagem do Matplotlib para calcular e desenhar o histograma correspondente.
-   **Carregamento**: A imagem de entrada é carregada diretamente em escala de cinza.
-   **Processamento**: As operações de equalização e negativo são aplicadas à imagem original.
-   **Visualização**: O script cria uma grade de plotagem de 3x2 com o Matplotlib. Em cada linha, a imagem processada é mostrada na coluna da esquerda e seu histograma correspondente é mostrado na coluna da direita.

## Dependências

Para executar este script, você precisará das seguintes bibliotecas Python:

-   `opencv-python`
-   `numpy`
-   `matplotlib`

Você pode instalar todas com um único comando via `pip`:
`
pip install opencv-python numpy matplotlib`

## Como Usar

1.  **Preparar o Ambiente**:
    * Salve o código como `histogramas.py`.
    * Coloque uma imagem para análise no mesmo diretório do script e nomeie-a como `imagem4.jpg` (ou altere o nome do arquivo diretamente no código).

2.  **Executar o Script**:
    * Abra um terminal e execute o código:
        ```bash
        python histogramas.py
        ```

3.  **Analisar o Resultado**:
    * Uma janela do Matplotlib será aberta, exibindo uma figura com 6 gráficos:
        * **Linha 1**: Imagem Original e seu Histograma.
        * **Linha 2**: Imagem Equalizada e seu Histograma.
        * **Linha 3**: Imagem Negativa e seu Histograma.
    * Isso permite uma comparação direta do efeito de cada transformação na imagem e em sua distribuição de pixels.


