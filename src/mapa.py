# mapa.py

from .cidade import Cidade

class Mapa:
    """Gerencia todas as cidades e suas conexões no jogo."""

    def __init__(self):
        self.cidades = {}  # Dicionário para acesso rápido às cidades pelo nome

    def adicionar_cidade(self, nome_cidade: str):
        """Adiciona uma nova cidade ao mapa."""
        if nome_cidade not in self.cidades:
            cidade = Cidade(nome_cidade)
            self.cidades[nome_cidade] = cidade

    def adicionar_conexao(self, cidade1_nome: str, cidade2_nome: str):
        """Cria uma conexão de mão dupla entre duas cidades."""
        if cidade1_nome in self.cidades and cidade2_nome in self.cidades:
            cidade1 = self.cidades[cidade1_nome]
            cidade2 = self.cidades[cidade2_nome]
            cidade1.adicionar_vizinho(cidade2)
            cidade2.adicionar_vizinho(cidade1)
        else:
            print("Erro: Uma ou ambas as cidades não existem no mapa.")

    def get_cidade(self, nome_cidade: str) -> Cidade:
        """Retorna um objeto Cidade pelo nome."""
        return self.cidades.get(nome_cidade)