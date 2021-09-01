from atividade1.src.Impostos.Contracts.IImposto import IImposto

class Iof(IImposto):

    def __init__(self, valorBruto):
        self.__valorBruto = valorBruto

    def calcular(self):
        return self.__valorBruto * 0.18