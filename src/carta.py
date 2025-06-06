# cartas.py

import random

class Carta:
    """Classe base para todas as cartas do jogo."""

    def __init__(self, nome: str):
        self.nome = nome

    def __str__(self):
        return f"Carta: {self.nome}"


class CartaCidade(Carta):
    """Representa uma carta de cidade."""

    def __init__(self, nome: str, populacao: int):
        super().__init__(nome)
        self.populacao = populacao

    def __str__(self):
        return f"Carta Cidade: {self.nome} (Pop: {self.populacao})"


class CartaEvento(Carta):
    """Representa uma carta de evento."""

    def __init__(self, nome: str, habilidade: str):
        super().__init__(nome)
        self.habilidade = habilidade

    def __str__(self):
        return f"Carta Evento: {self.nome} - {self.habilidade}"


class CartaEpidemia(Carta):
    """Representa uma carta de epidemia."""

    def __init__(self):
        super().__init__("Epidemia")

    def __str__(self):
        return "!!! EPIDEMIA !!!"


class CartaPersonagem(Carta):
    """Representa uma carta de personagem (papel)."""

    def __init__(self, nome: str, habilidade: str):
        super().__init__(nome)
        self.habilidade = habilidade

    def __str__(self):
        return f"Personagem: {self.nome} - {self.habilidade}"


class Baralho:
    """Representa um baralho de cartas no jogo."""

    def __init__(self, cartas: list):
        self.cartas = cartas
        self.descarte = []
        self.embaralhar()

    def embaralhar(self):
        """Embaralha as cartas no baralho."""
        random.shuffle(self.cartas)
        print("Baralho embaralhado.")

    def comprar_carta(self):
        """Retira uma carta do topo do baralho."""
        if len(self.cartas) > 0:
            return self.cartas.pop(0)
        else:
            print("O baralho está vazio!")
            return None

    def adicionar_ao_descarte(self, carta: Carta):
        """Adiciona uma carta à pilha de descarte."""
        self.descarte.append(carta)