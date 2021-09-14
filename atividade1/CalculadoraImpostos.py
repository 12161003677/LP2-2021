from typing import Type
from Impostos.Contratacts.IImposto import IImposto

class CalculadoraImpostos:

    def __init__(self, imposto: Type[IImposto]):
        self.__imposto = imposto

    def calcular(self):
        return self.__imposto.calcular()