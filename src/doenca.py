# doenca.py

class Doenca:

  def __init__(self, cor: str):
    self.cor = cor
    self.curada = False
  
  def __str__(self):
    status_cura = "Curada" if self.curada else "Não Curada"
    return f"Doença {self.cor} - {status_cura}"