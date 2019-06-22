class Resposta:
  def __init__(self, idade, escolaridade, aceita, porque, substituicao):
    self.idade = idade
    self.escolaridade = escolaridade
    self.aceita = aceita
    self.porque = porque
    self.substituicao = substituicao

respostas = []

class AceitacaoPorcentagem:
  sim = 0
  nao = 0
  depende = 0
