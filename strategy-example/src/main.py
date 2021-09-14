from CalculadoraImpostos import CalculadoraImpostos
from Impostos import Iof, Icms

if __name__ == '__main__':
    valorBruto = 1000;
    icms = Icms(valorBruto)
    iof = Iof(valorBruto)

    print("O ICMS de {} é: {}".format(valorBruto, CalculadoraImpostos(icms).calcular()))
    print("O IOF de {} é: {}".format(valorBruto, CalculadoraImpostos(iof).calcular()))
