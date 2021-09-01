class Conta:
    __codigoBanco = '001'

    def __init__(self, numero, titular, saldo, limite):

        self.__numero = numero
        self.__titular = titular
        self.__limite = limite
        self.__saldo = saldo

    def imprimirSaldo(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

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
        return self.__saldo

    # métodos estáticos
    @staticmethod
    def codigBanco():
        return Conta.__codigoBanco