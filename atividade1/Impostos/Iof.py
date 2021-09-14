from .Contratacts.IImposto import IImposto

class Iof(IImposto):
    def __init__(self, valorBruto):
        self.__valorBruto = valorBruto

    def calcular(self):
        return self.__valorBruto * 0.018
