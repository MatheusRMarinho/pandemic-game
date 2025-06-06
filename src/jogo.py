# jogo.py

from .mapa import Mapa
from .jogador import Jogador
from .carta import Baralho, CartaCidade, CartaEpidemia
from .acao import Acao

class Jogo:
    """
    Classe principal que gerencia o estado e as regras do jogo.
    Implementa o Padrão GoF Facade, fornecendo uma interface
    simplificada para as operações do jogo.
    """
    def __init__(self, nomes_jogadores: list, nomes_cidades: list):
        print("Iniciando o jogo Pandemic!")
        self.mapa = self._inicializar_mapa(nomes_cidades)
        self.baralho_jogadores = self._inicializar_baralho_jogadores(nomes_cidades)
        self.jogadores = self._inicializar_jogadores(nomes_jogadores)
        self.doencas_curadas = []
        self.turno_atual = 0

    def _inicializar_mapa(self, nomes_cidades: list) -> Mapa:
        mapa = Mapa()
        for nome in nomes_cidades:
            mapa.adicionar_cidade(nome)
        # Conexões simplificadas para exemplo
        mapa.adicionar_conexao("São Paulo", "Rio de Janeiro")
        mapa.adicionar_conexao("Rio de Janeiro", "Belo Horizonte")
        mapa.adicionar_conexao("Belo Horizonte", "São Paulo")
        mapa.adicionar_conexao("São Paulo", "Atlanta") # Conexão internacional de exemplo
        return mapa

    def _inicializar_baralho_jogadores(self, nomes_cidades: list) -> Baralho:
        cartas = [CartaCidade(nome, 10000) for nome in nomes_cidades]
        # Adicionar cartas de epidemia
        for _ in range(4): # Número de epidemias para o exemplo
            cartas.append(CartaEpidemia())
        return Baralho(cartas)

    def _inicializar_jogadores(self, nomes_jogadores: list) -> list[Jogador]:
        jogadores = []
        cidade_inicial = self.mapa.get_cidade("Atlanta") # Todas começam em Atlanta
        if not cidade_inicial:
            # Fallback se Atlanta não estiver na lista de cidades
            primeira_cidade = list(self.mapa.cidades.values())[0]
            cidade_inicial = primeira_cidade
            self.mapa.adicionar_cidade("Atlanta") # Adiciona para garantir
            self.mapa.adicionar_conexao("Atlanta", primeira_cidade.nome)


        for nome in nomes_jogadores:
            jogador = Jogador(nome, cidade_inicial)
            # Distribuir cartas iniciais
            for _ in range(2):
                carta = self.baralho_jogadores.comprar_carta()
                if carta:
                    jogador.adicionar_carta_a_mao(carta)
            jogadores.append(jogador)
        return jogadores

    def executar_acao(self, jogador: Jogador, acao: Acao, **kwargs):
        """Executa uma ação para um jogador."""
        print("-" * 20)
        print(f"TURNO DE {jogador.nome}: Executando ação {acao.__class__.__name__}")
        acao.executa(**kwargs)
        print("-" * 20)


class Turno:
    """Gerencia as fases de um turno de um jogador."""
    def __init__(self, jogador: Jogador, jogo: Jogo):
        self.jogador = jogador
        self.jogo = jogo
        self.acoes_restantes = 4

    def iniciar_turno(self):
        print(f"\n{'='*30}\nInício do turno de {self.jogador.nome}\n{'='*30}")
        self.fase_acoes()
        self.fase_comprar_cartas()
        self.fase_infeccao()

    def fase_acoes(self):
        """Simula o jogador realizando suas 4 ações."""
        print(f"--- FASE DE AÇÕES ({self.jogador.nome}) ---")
        # Exemplo de ações a serem tomadas
        # Aqui o jogador escolheria as ações. Estamos simulando algumas.
        pass # A simulação será feita no main.py

    def fase_comprar_cartas(self):
        """O jogador compra 2 cartas."""
        print(f"--- FASE DE COMPRAR CARTAS ({self.jogador.nome}) ---")
        for _ in range(2):
            carta = self.jogo.baralho_jogadores.comprar_carta()
            if isinstance(carta, CartaEpidemia):
                print("!!! JOGADOR COMPROU UMA CARTA DE EPIDEMIA !!!")
                # Lógica de epidemia (simplificada)
            elif carta:
                self.jogador.adicionar_carta_a_mao(carta)

    def fase_infeccao(self):
        """Revela cartas de infecção para adicionar cubos de doença."""
        print(f"--- FASE DE INFECÇÃO ---")
        taxa_infeccao = 2 # Exemplo
        for i in range(taxa_infeccao):
            cidade_infectada_nome = list(self.jogo.mapa.cidades.keys())[i] # Simplificado
            cidade = self.jogo.mapa.get_cidade(cidade_infectada_nome)
            if cidade:
                cidade.doencas += 1
                print(f"Infecção em {cidade.nome}! Total de doenças: {cidade.doencas}")