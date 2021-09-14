from CalculadoraImpostos import CalculadoraImpostos
from Impostos.Icms import Icms
from Impostos.Iof import Iof

if __name__ == '__main__':
    valorBruto = 1000
    iof = Iof(valorBruto)
    icms = Icms(valorBruto)

    print("o icms de {} é: {}".format(valorBruto, CalculadoraImpostos(icms).calcular()))
    print("o iof de {} é: {}".format(valorBruto, CalculadoraImpostos(iof).calcular()))