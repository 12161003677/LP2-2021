from typing import Type
from Impostos import IImposto

class CalculadoraImpostos:
    def __init__(self, imposto: Type[IImposto]):
        self.imposto = imposto

    def calcular(self):
        return self.imposto.calcular()
