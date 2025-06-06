# jogador.py

from .cidade import Cidade
from .carta import Carta

class Jogador:
    """Representa um jogador no jogo."""

    def __init__(self, nome: str, cidade_inicial: Cidade):
        self.nome = nome
        self.localizacao_atual = cidade_inicial
        self.mao = []  # Lista de objetos Carta

    def adicionar_carta_a_mao(self, carta: Carta):
        """Adiciona uma carta à mão do jogador."""
        self.mao.append(carta)
        print(f"{self.nome} recebeu a carta: {carta.nome}")

    def mover(self, nova_cidade: Cidade):
        """Move o jogador para uma nova cidade."""
        self.localizacao_atual = nova_cidade
        print(f"{self.nome} moveu-se para {nova_cidade.nome}.")

    def __str__(self):
        cartas_na_mao = ", ".join([carta.nome for carta in self.mao])
        return (
            f"Jogador: {self.nome}\n"
            f"Localização: {self.localizacao_atual.nome}\n"
            f"Mão: [{cartas_na_mao}]"
        )