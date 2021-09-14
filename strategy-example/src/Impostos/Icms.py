from .Contracts.IImposto import IImposto

class Icms(IImposto):

    def __init__(self, valorBruto):
        self.__valorBruto = valorBruto

    def calcular(self):
        return self.__valorBruto * 0.15