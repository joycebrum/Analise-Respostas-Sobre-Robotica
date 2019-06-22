from variables import Resposta
from variables import respostas
from variables import AceitacaoPorcentagem


EFC = "Ensino Fundamental Incompleto"
EFI = "Ensino Fundamental Completo"
EMC = "Ensino Medio Completo"
EMI = "Ensino Medio Incompleto"
ESC = "Ensino Superior Completo"
ESI = "Ensino Superior Incompleto"

def aceitacaoPorEscolaridade():
    quant = len(respostas)
    totalRespostasPorEscolaridade = {
        EFC: 0,
        EFI: 0,
        EMC: 0,
        EMI: 0,
        ESC: 0,
        ESI: 0
    }
    aceitaPorEscolaridade = {
        EFC: AceitacaoPorcentagem(),
        EFI: AceitacaoPorcentagem(),
        EMC: AceitacaoPorcentagem(),
        EMI: AceitacaoPorcentagem(),
        ESC: AceitacaoPorcentagem(),
        ESI: AceitacaoPorcentagem()
    }
    for resposta in respostas :
        totalRespostasPorEscolaridade[resposta.escolaridade] += 1
        if resposta.aceita == "Sim":
          aceitaPorEscolaridade[resposta.escolaridade].sim += 1
        elif resposta.aceita == "Nao":
          aceitaPorEscolaridade[resposta.escolaridade].nao += 1
        else:
          aceitaPorEscolaridade[resposta.escolaridade].depende +=1

    print("\nAceitação por escolaridade")
    for key,val in aceitaPorEscolaridade.items():
      print("\nEscolaridade: ", key, " Total: ", totalRespostasPorEscolaridade[key])
      print("{ sim: ", val.sim, ", nao: ", val.nao, ", depende: ", val.depende, " }")

    print("\nPorcentagem de aceitação por escolaridade")
    for key,val in aceitaPorEscolaridade.items():
      print("\nEscolaridade: ", key, " Total: ", totalRespostasPorEscolaridade[key])
      val.sim = 100 * val.sim / totalRespostasPorEscolaridade[key]
      val.nao = 100 * val.nao / totalRespostasPorEscolaridade[key]
      val.depende = 100 * val.depende / totalRespostasPorEscolaridade[key]
      print("{ sim: ", val.sim, ", nao: ", val.nao, ", depende: ", val.depende, " }")

