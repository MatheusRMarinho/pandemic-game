# cidade.py

class Cidade:
    """Representa uma cidade no tabuleiro do jogo."""

    def __init__(self, nome: str):
        self.nome = nome
        self.doencas = 0
        self.centro_pesquisa = False
        self.vizinhos = []  # Lista de objetos Cidade

    def adicionar_vizinho(self, vizinho):
        """Adiciona uma cidade vizinha a esta cidade."""
        if vizinho not in self.vizinhos:
            self.vizinhos.append(vizinho)

    def __str__(self):
        return (
            f"Cidade: {self.nome} | Doenças: {self.doencas} | "
            f"Centro de Pesquisa: {'Sim' if self.centro_pesquisa else 'Não'}"
        )