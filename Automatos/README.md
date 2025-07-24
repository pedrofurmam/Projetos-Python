# Simulador de Autômato Finito: Colheitadeira Autônoma

Este projeto implementa um **Autômato Finito Determinístico (AFD)** em Python para simular o ciclo de operações de uma colheitadeira agrícola autônoma. O objetivo é modelar os diferentes estados da máquina — desde ser ligada até completar um ciclo de colheita e plantio — e as transições entre esses estados com base em uma sequência de comandos (a "fita" de entrada).

## O que é um Autômato Finito?

Um Autômato Finito é um modelo matemático de computação que consiste em:
- Um conjunto de **estados**.
- Um **estado inicial**.
- Um conjunto de **estados finais** (ou de aceitação).
- Um conjunto de **transições** que ditam para qual estado o autômato se moverá a partir de seu estado atual, dado um determinado símbolo de entrada.

O autômato processa uma sequência de símbolos (chamada de "palavra" ou "fita") e, ao final, se ele estiver em um estado final, a palavra é "aceita". Caso contrário, ou se uma transição inválida for encontrada, a palavra é "rejeitada".

## Sobre o Autômato da Colheitadeira

Este simulador modela o comportamento de uma máquina agrícola complexa. A máquina não apenas colhe, mas também transporta, descarrega, planta e lida com obstáculos em seu caminho.

### Estados Possíveis

O autômato pode estar em um dos seguintes estados:

-   `Desligada`: O estado inicial. A máquina está inoperante.
-   `Inicializando`: A máquina está ligando seus sistemas.
-   `VerificandoSistema`: Checagem de diagnóstico dos componentes.
-   `Pronta`: Sistemas verificados e prontos para iniciar o ciclo de trabalho.
-   `AreaColheita`: Posicionada na área designada para a colheita.
-   `PreparandoColheita`: Preparando os mecanismos de corte e armazenamento.
-   `Colhendo`: Em processo ativo de colheita.
-   `TransportandoCarga`: A colheita foi concluída e a carga está sendo transportada.
-   `Descarga`: Descarregando o material colhido.
-   `VerificandoSolo`: Analisando as condições do solo para o plantio.
-   `Plantando`: Semeando uma nova cultura.
-   `Retornando`: Voltando à base ou ao ponto de partida.
-   `FinalizandoCiclo`: O ciclo completo foi bem-sucedido. **(Estado Final)**
-   `ParadaEmergencia`: Uma falha no sistema foi detectada, e a máquina parou por segurança.
-   `ObstaculoDetectado`: Um obstáculo foi encontrado no caminho.
-   `DesviandoEsquerda`/`DesviandoDireita`: Realizando manobra para desviar do obstáculo.
-   `RotaCorrigida`: Rota recalculada após o desvio.

### Símbolos (Comandos)

As transições entre os estados são acionadas pelos seguintes símbolos de entrada:

-   `Ligar`, `Desligar`
-   `Verificar`, `SistemaOk`, `SistemaFalha`
-   `IniciarCiclo`, `IniciarColheita`, `CargaCompleta`, `IniciarDescarga`
-   `DetectarPlantio`, `SoloOk`, `Retornar`, `Fim`
-   `Desvio`, `ObstaculoEsquerda`, `ObstaculoDireita`, `CorrigirRota`

## Estrutura do Código

O script principal é dividido em quatro partes:

1.  **Definição dos Estados**:
    -   `final_states`: Um conjunto (`set`) contendo os estados de aceitação.
    -   `initial_state`: Uma string que define o ponto de partida do autômato.

2.  **Função de Transição (`transitions`)**:
    -   Um dicionário que mapeia uma tupla `(estado_atual, simbolo_lido)` para um `proximo_estado`.

3.  **Processador do Autômato (`processar_fita`)**:
    -   Uma função que recebe uma lista de símbolos (`fita`).
    -   Ela itera sobre a fita, atualizando o estado do autômato.
    -   Ao final, informa se a sequência foi aceita ou rejeitada.

4.  **Entrada do Usuário**:
    -   A parte final do script que solicita ao usuário uma sequência de comandos e a processa.

## Como Executar

1.  Certifique-se de ter o Python instalado.
2.  Salve o código em um arquivo (por exemplo, `automato_colheitadeira.py`).
3.  Execute o arquivo pelo terminal:
    ```bash
    python automato_colheitadeira.py
    ```
4.  O programa solicitará que você digite a fita. Insira os símbolos separados por espaços e pressione Enter.

### Exemplos de Uso

#### Exemplo 1: Ciclo de Sucesso

Esta sequência simula um ciclo completo e bem-sucedido, que deve ser **aceito**.

**Entrada:**

Ligar Verificar SistemaOk IniciarCiclo IniciarColheita IniciarColheita CargaCompleta IniciarDescarga DetectarPlantio SoloOk Plantando Retornar Fim

**Saída Esperada:**
Estado inicial: Desligada

Desligada --[Ligar]--> Inicializando
Inicializando --[Verificar]--> VerificandoSistema
VerificandoSistema --[SistemaOk]--> Pronta
Pronta --[IniciarCiclo]--> AreaColheita
AreaColheita --[IniciarColheita]--> PreparandoColheita
PreparandoColheita --[IniciarColheita]--> Colhendo
Colhendo --[CargaCompleta]--> TransportandoCarga
TransportandoCarga --[IniciarDescarga]--> Descarga
Descarga --[DetectarPlantio]--> VerificandoSolo
VerificandoSolo --[SoloOk]--> Plantando
Plantando --[Retornar]--> Retornando
Retornando --[Fim]--> FinalizandoCiclo

✅ Palavra aceita. Estado final: FinalizandoCiclo


#### Exemplo 2: Sequência Inválida

Esta sequência tenta uma ação impossível a partir do estado atual, resultando em uma transição inválida. A palavra será **rejeitada**.

**Entrada:**
IniciarCiclo IniciarColheita


**Saída Esperada:**
Estado inicial: Desligada

Desligada --[IniciarCiclo]--> ❌ Transição inválida.

❌ Palavra rejeitada.
