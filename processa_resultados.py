import csv
from random import randint
from analiseIdade import aceitacaoPorIdade
from variables import respostas
from variables import Resposta
from analiseEscolaridade import aceitacaoPorEscolaridade

def imprime(resposta):
    print("\n")
    print("Idade ", resposta.idade)
    print("Escolaridade ", resposta.escolaridade)
    print("Aceitaria fazer uma cirurgia por robô? ", resposta.aceita)
    print("Por que? ", resposta.porque)
    print("O que você acha sobre a substituição completa de humanos por robôs na medicina? ", resposta.substituicao)
    
with open('dados.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    cabecalho = True
    for row in csv_reader:
        if cabecalho:
            cabecalho = False
        else:
            respostas.append(Resposta(row[1], row[2], row[3], row[4], row[5]))
    
    print ("\n---------------------------- IDADE --------------------------------\n")
    aceitacaoPorIdade();
    print ("\n-------------------------- ESCOLARIDADE ----------------------------\n")
    aceitacaoPorEscolaridade()
    print ("\n ------------------------- EXEMPLOS -------------------------------\n")
    i = 0
    while i < 5:
      position = randint(0, len(respostas))
      imprime(respostas[position])
      i = i + 1
      

