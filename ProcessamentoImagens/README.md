# Detector de Moedas com OpenCV

Este projeto utiliza técnicas de processamento de imagem com a biblioteca OpenCV em Python para detectar moedas do Real brasileiro em uma imagem, classificá-las de acordo com seu valor e calcular a soma total.

O script implementa uma abordagem híbrida em duas etapas para maximizar a precisão da detecção:
1.  **Detecção de Círculos (Hough Transform)**: Identifica a maioria das moedas com base em sua forma circular.
2.  **Correspondência de Padrão (Template Matching)**: Atua como um refinamento para encontrar moedas específicas que a primeira etapa possa ter perdido.

## Funcionalidades

-   Detecta moedas de R$ 1,00, R$ 0,50, R$ 0,25 e R$ 0,10.
-   Classifica as moedas com base em uma combinação de **raio (tamanho)** e **cor (matiz e saturação)**.
-   Utiliza uma abordagem de duas fases para melhorar a detecção.
-   Calcula e exibe o valor total das moedas detectadas.
-   Gera uma imagem de resultado com as moedas demarcadas e seus valores identificados.

## Como Funciona

O fluxo de trabalho do script é dividido em duas etapas principais:

### Etapa 1: Detecção Principal com `HoughCircles`

1.  **Carregamento e Pré-processamento**:
    -   A imagem de entrada (ex: `moedas5.jpeg`) é carregada.
    -   É convertida para a escala de cinza e um filtro de desfoque (Gaussian Blur) é aplicado para reduzir ruídos e facilitar a detecção de círculos.
    -   Uma cópia da imagem no espaço de cores HSV também é criada para análise de cor.

2.  **Detecção de Círculos**:
    -   A função `cv2.HoughCircles` é aplicada na imagem desfocada para encontrar todas as formas circulares que se encaixam em uma faixa de raio pré-definida.

3.  **Classificação e Validação**:
    -   Para cada círculo detectado, o script:
        -   Extrai a região de interesse (ROI) da moeda.
        -   Calcula a média de **Matiz (Hue)** e **Saturação (Saturation)** dentro da ROI.
        -   Usa um conjunto de regras (`if/elif`) para classificar o valor da moeda (R$ 1,00, R$ 0,50, R$ 0,25, R$ 0,10) com base no seu **raio** e nas características de **cor**. Moedas prateadas, por exemplo, possuem baixa saturação, enquanto moedas douradas/acobreadas possuem matiz e saturação específicos.

### Etapa 2: Refinamento com `TemplateMatching` (Opcional)

Esta etapa serve como uma "segunda chance" para encontrar moedas que a Transformada de Hough pode não ter detectado corretamente.

1.  **Carregamento do Template**:
    -   O script tenta carregar uma imagem de modelo (ex: `template_10_centavos_faltante.png`), que é um recorte de uma moeda específica.

2.  **Busca por Correspondência**:
    -   A função `cv2.matchTemplate` "desliza" a imagem do modelo sobre a imagem principal (em escala de cinza) para encontrar áreas com alta similaridade.

3.  **Validação de Nova Moeda**:
    -   Para cada correspondência encontrada, o script verifica se a localização já foi identificada na Etapa 1.
    -   Se for uma detecção nova, a moeda é marcada (neste caso, com um círculo amarelo para diferenciação) e seu valor é adicionado ao total.

## Dependências

Para executar este script, você precisará das seguintes bibliotecas Python:

-   `opencv-python`
-   `numpy`

Você pode instalá-las usando `pip`:

`pip install opencv-python numpy`

Execute o script através do terminal:

`python detectoresmoedas.py`
