# Conjunto de estados finais
final_states = {"FinalizandoCiclo"}

# Estado inicial
initial_state = "Desligada"

# Função de transição
transitions = {
    ("Desligada", "Ligar"): "Inicializando",
    ("Inicializando", "Verificar"): "VerificandoSistema",
    ("VerificandoSistema", "SistemaOk"): "Pronta",
    ("VerificandoSistema", "SistemaFalha"): "ParadaEmergencia",
    ("ParadaEmergencia", "Desligar"): "Desligada",

    ("Pronta", "IniciarCiclo"): "AreaColheita",
    ("AreaColheita", "IniciarColheita"): "PreparandoColheita",
    ("PreparandoColheita", "IniciarColheita"): "Colhendo",
    ("Colhendo", "CargaCompleta"): "TransportandoCarga",
    ("TransportandoCarga", "IniciarDescarga"): "Descarga",
    ("Descarga", "DetectarPlantio"): "VerificandoSolo",
    ("VerificandoSolo", "SoloOk"): "Plantando",
    ("Plantando", "Retornar"): "Retornando",
    ("Retornando", "Fim"): "FinalizandoCiclo",

    # Desvios e obstáculos
    ("Colhendo", "Desvio"): "ObstaculoDetectado",
    ("Plantando", "Desvio"): "ObstaculoDetectado",
    ("TransportandoCarga", "Desvio"): "ObstaculoDetectado",
    ("ObstaculoDetectado", "ObstaculoEsquerda"): "DesviandoEsquerda",
    ("ObstaculoDetectado", "ObstaculoDireita"): "DesviandoDireita",
    ("DesviandoEsquerda", "CorrigirRota"): "RotaCorrigida",
    ("DesviandoDireita", "CorrigirRota"): "RotaCorrigida",
    ("RotaCorrigida", "IniciarColheita"): "Colhendo",
    ("RotaCorrigida", "CargaCompleta"): "TransportandoCarga",
    ("RotaCorrigida", "SoloOk"): "Plantando",
}

def processar_fita(fita):
    estado_atual = initial_state
    print(f"\nEstado inicial: {estado_atual}\n")

    for simbolo in fita:
        chave = (estado_atual, simbolo)
        if chave in transitions:
            proximo_estado = transitions[chave]
            print(f"{estado_atual} --[{simbolo}]--> {proximo_estado}")
            estado_atual = proximo_estado
        else:
            print(f"{estado_atual} --[{simbolo}]--> ❌ Transição inválida.")
            print("\n❌ Palavra rejeitada.")
            return

    if estado_atual in final_states:
        print(f"\n✅ Palavra aceita. Estado final: {estado_atual}")
    else:
        print(f"\n❌ Palavra rejeitada. Estado final: {estado_atual}")

# Entrada do usuário
entrada = input("Digite a fita (símbolos separados por espaço):\n> ").strip().split()
processar_fita(entrada)
