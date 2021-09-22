from abc import ABC
from collections.abc import MutableSequence

class Conta:
    __codigoBanco = '001'

    def __init__(self, numero, titular, saldo, limite):

        self._numero = numero
        self._titular = titular
        self._limite = limite
        self._saldo = saldo

    def imprimirSaldo(self):
        print("Saldo de {} do titular {}".format(self._saldo, self._titular))

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    # getters e setters
    def getNumero(self):
        return self._numero

    def setNumero(self, numero):
        self._numero = numero

    def getTitular(self):
        return self._titular

    def setTitular(self, titular):
        self._titular = titular

    def getLimite(self):
        return self._limite

    def setLimite(self, limite):
        self._limite = limite

    # properties
    @property
    def limite(self):
        return self._limite

    @limite.setter
    def limite(self, limite):
        self._limite = limite

    @property
    def saldo(self):
        return self._saldo

    # métodos estáticos
    @staticmethod
    def codigBanco():
        return Conta.__codigoBanco

class ContaCorrente(Conta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)
        self._taxaOperacao = 0.01
        print('Iniciando Conta Corrente')

    def getTaxaOperacao(self):
        return self._taxaOperacao

    def debitarTaxaOperacao(self, valor):
        self._saldo -=  valor*self._taxaOperacao

    def imprimir(self):
        print("Taxa de operação da conta é {} e o saldo é {}".format(self._taxaOperacao, self.saldo))

    def __str__(self):
        return f'{self._numero} | {self._titular} | {self._limite} | {self._saldo} | {self._taxaOperacao}'

class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)
        self._taxaRendimento = 0.0001
        print('Iniciando Conta Poupança')

    def getTaxaRendimento(self):
        return self._taxaRendimento

    def creditarRendimento(self):
        self._saldo += self._saldo * self._taxaRendimento

    def imprimir(self):
        print("Taxa de rendimento da conta é {} e o saldo é {}".format(self._taxaRendimento, self.saldo))

    def __str__(self):
        return f'{self._numero} | {self._titular} | {self._limite} | {self._saldo} | {self._taxaRendimento}'

class ContaPoupancaEspecial(ContaPoupanca, ContaCorrente):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)
        print('Iniciando Conta Poupança Especial')

    def imprimir(self):
        print("Taxa de operação da conta é {}".format(self._taxaOperacao))
        print("Taxa de rendimento da conta é {}".format(self._taxaRendimento))
        print("O saldo é {}".format(self.saldo))


class ListaContas(MutableSequence):
    def __init__(self, contas):
        self.__contas = contas

    def __getitem__(self, key):
        return self.__contas[key]

    def __len__(self):
        return len(self.__contas)

    def __delitem__(self, key):
        self.__contas.pop(key)
        print("O item {} foi removido".format(key))

    def __setitem__(self, key, item):
        self.__contas[key] = item
        print("O item {} foi alterado".format(key))

    def insert(self, item):
        self.__contas.append(item)