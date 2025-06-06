# acoes.py

from abc import ABC, abstractmethod

class Acao(ABC):
    """Classe base abstrata para todas as ações do jogador."""

    def __init__(self, jogador):
        self.jogador = jogador

    @abstractmethod
    def executa(self, **kwargs):
        """
        Método abstrato para executar a ação.
        Este é o núcleo do Padrão GRASP Polymorphism.
        """
        pass


class Mover(Acao):
    """Ação de mover o jogador entre cidades."""
    def executa(self, **kwargs):
        destino = kwargs.get('destino')
        if destino and destino in self.jogador.localizacao_atual.vizinhos:
            self.jogador.mover(destino)
        else:
            print(f"Não é possível mover para {destino.nome if destino else 'um destino inválido'}.")


class ConstruirCentro(Acao):
    """Ação de construir um centro de pesquisa."""
    def executa(self, **kwargs):
        cidade_atual = self.jogador.localizacao_atual
        if not cidade_atual.centro_pesquisa:
            cidade_atual.centro_pesquisa = True
            print(f"Centro de pesquisa construído em {cidade_atual.nome}!")
        else:
            print(f"Já existe um centro de pesquisa em {cidade_atual.nome}.")


class TratarDoenca(Acao):
    """Ação de tratar uma doença em uma cidade."""
    def executa(self, **kwargs):
        cidade_atual = self.jogador.localizacao_atual
        if cidade_atual.doencas > 0:
            cidade_atual.doencas -= 1
            print(f"Uma doença foi tratada em {cidade_atual.nome}. Restam: {cidade_atual.doencas}")
        else:
            print(f"Não há doenças para tratar em {cidade_atual.nome}.")


class Compartilhar(Acao):
    """Ação de compartilhar conhecimento (cartas)."""
    def executa(self, **kwargs):
        outro_jogador = kwargs.get('outro_jogador')
        carta = kwargs.get('carta')
        print(f"{self.jogador.nome} compartilhou a carta {carta.nome} com {outro_jogador.nome}.")


class DesenvolverCura(Acao):
    """Ação de desenvolver a cura para uma doença."""
    def executa(self, **kwargs):
        cidade_atual = self.jogador.localizacao_atual
        if cidade_atual.centro_pesquisa:
            print(f"{self.jogador.nome} desenvolveu uma cura!")
        else:
            print(f"É necessário estar em uma cidade com centro de pesquisa para desenvolver a cura.")