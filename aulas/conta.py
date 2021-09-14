class Conta:
    __codigoBanco = '001'

    def __init__(self, numero, titular, saldo, limite):

        self.__numero = numero
        self.__titular = titular
        self.__limite = limite
        self._saldo = saldo

    def imprimirSaldo(self):
        print("Saldo de {} do titular {}".format(self._saldo, self.__titular))

    def depositar(self, valor):
        self._saldo += valor

    def sacar(self, valor):
        self._saldo -= valor

    # getters e setters
    def getNumero(self):
        return self.__numero

    def setNumero(self, numero):
        self.__numero = numero

    def getTitular(self):
        return self.__titular

    def setTitular(self, titular):
        self.__titular = titular

    def getLimite(self):
        return self.__limite

    def setLimite(self, limite):
        self.__limite = limite

    # properties
    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

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
        self.__taxaOperacao = 0.01
        print('Iniciando Conta Corrente')

    def getTaxaOperacao(self):
        return self.__taxaOperacao

    def debitarTaxaOperacao(self, valor):
        self._saldo -=  valor*self.__taxaOperacao

    def imprimir(self):
        print("Taxa de operação da conta é {} e o saldo é {}".format(self.__taxaOperacao, self.saldo))


class ContaPoupanca(Conta):
    def __init__(self, numero, titular, saldo, limite):
        super().__init__(numero, titular, saldo, limite)
        self.__taxaRendimento = 0.0001
        print('Iniciando Conta Poupança')

    def getTaxaRendimento(self):
        return self.__taxaRendimento

    def creditarRendimento(self):
        self._saldo += self._saldo * self.__taxaRendimento

    def imprimir(self):
        print("Taxa de rendimento da conta é {} e o saldo é {}".format(self.__taxaRendimento, self.saldo))

