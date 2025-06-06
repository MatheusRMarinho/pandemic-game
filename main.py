# main.py

from src.jogo import Jogo, Turno
from src.jogador import Jogador
from src.acao import Mover, ConstruirCentro, TratarDoenca, DesenvolverCura

def simular_jogo():
    """Função principal para rodar uma simulação do jogo."""

    # 1. Configuração Inicial
    nomes_jogadores = ["Alice", "Beto"]
    nomes_cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Atlanta"]
    
    # A classe Jogo atua como Facade, simplificando a criação do jogo.
    jogo = Jogo(nomes_jogadores, nomes_cidades)

    # Jogadores e estado inicial
    alice = jogo.jogadores[0]
    beto = jogo.jogadores[1]
    
    print("\n--- ESTADO INICIAL DO JOGO ---")
    for jogador in jogo.jogadores:
        print(jogador)
    print("-" * 30)


    # 2. Simulação de um Turno (Turno da Alice)
    turno_alice = Turno(alice, jogo)
    
    print(f"\n{'='*30}\nINICIANDO TURNO DE {alice.nome.upper()}\n{'='*30}")

    # Alice realiza suas 4 ações (Polymorphism em ação)
    # Ação 1: Mover para uma cidade vizinha
    sp = jogo.mapa.get_cidade("São Paulo")
    # Para o exemplo, vamos mover Alice para São Paulo antes do turno.
    alice.mover(sp)

    # Ação 1 do turno: Tratar Doença
    # Primeiro, vamos adicionar uma doença para que a ação tenha efeito
    sp.doencas = 2
    print(f"Estado de {sp.nome} antes de tratar: {sp.doencas} doenças.")
    acao_tratar = TratarDoenca(alice)
    jogo.executar_acao(alice, acao_tratar)

    # Ação 2: Mover para o Rio de Janeiro
    rj = jogo.mapa.get_cidade("Rio de Janeiro")
    acao_mover = Mover(alice)
    jogo.executar_acao(alice, acao_mover, destino=rj)
    
    # Ação 3: Construir um Centro de Pesquisa
    acao_construir = ConstruirCentro(alice)
    jogo.executar_acao(alice, acao_construir)

    # Ação 4: Tentar desenvolver a cura
    acao_curar = DesenvolverCura(alice)
    jogo.executar_acao(alice, acao_curar)

    # Fim das ações, o objeto Turno continua com as próximas fases
    turno_alice.fase_comprar_cartas()
    turno_alice.fase_infeccao()

    print("\n--- ESTADO FINAL DO JOGO APÓS O TURNO DE ALICE ---")
    for jogador in jogo.jogadores:
        print(jogador)
    print("\n--- ESTADO DO MAPA ---")
    for cidade in jogo.mapa.cidades.values():
        print(cidade)


if __name__ == "__main__":
    simular_jogo()