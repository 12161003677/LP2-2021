class Conta:

    def __init__(self, numero, titular, saldo, limite):

        # atributos publicos
        self.numero = numero
        self.titular = titular
        self.limite = limite

        # atributos privados
        self.__saldo = saldo

    def imprimirSaldo(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor