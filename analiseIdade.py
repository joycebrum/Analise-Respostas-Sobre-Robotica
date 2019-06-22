from variables import Resposta
from variables import respostas
from variables import AceitacaoPorcentagem

MENOS18 = "Menos de 18"
EH18E21 = "Entre 18 e 21 anos"
EH22E25 = "Entre 22 e 25 anos"
EH25E30 = "Entre 25 e 30 anos"
EH31E60 = "Entre 31 e 60 anos"
MAIS60 = "Acima de 60 anos"

def aceitacaoPorIdade():
    
    quant = len(respostas)
    totalRespostasPorIdade = {
        MENOS18: 0,
        EH18E21: 0,
        EH22E25: 0,
        EH25E30: 0,
        EH31E60: 0,
        MAIS60: 0
    }
    aceitaPorIdade = {
        MENOS18: AceitacaoPorcentagem(),
        EH18E21: AceitacaoPorcentagem(),
        EH22E25: AceitacaoPorcentagem(),
        EH25E30: AceitacaoPorcentagem(),
        EH31E60: AceitacaoPorcentagem(),
        MAIS60: AceitacaoPorcentagem()
    }
    for resposta in respostas :
        totalRespostasPorIdade[resposta.idade] += 1
        if resposta.aceita == "Sim":
          aceitaPorIdade[resposta.idade].sim += 1
        elif resposta.aceita == "Nao":
          aceitaPorIdade[resposta.idade].nao += 1
        else:
          aceitaPorIdade[resposta.idade].depende +=1
    
    print("\nAceitação por idade")
    for key,val in aceitaPorIdade.items():
      print("\nIdade: ", key, " Total: ", totalRespostasPorIdade[key])
      print("{ sim: ", val.sim, ", nao: ", val.nao, ", depende: ", val.depende, " }")

    print("\nPorcentagem de aceitação por idade")
    for key,val in aceitaPorIdade.items():
      print("\nIdade: ", key, " Total: ", totalRespostasPorIdade[key])
      val.sim = 100 * val.sim / totalRespostasPorIdade[key]
      val.nao = 100 * val.nao / totalRespostasPorIdade[key]
      val.depende = 100 * val.depende / totalRespostasPorIdade[key]
      print("{ sim: ", val.sim, ", nao: ", val.nao, ", depende: ", val.depende, " }")
