from conta import Conta

if __name__ == '__main__':
    conta1 = Conta(199249, 'ELIEZER ALVES', 250, 5000.00)

    conta1.imprimirSaldo()
    conta1.sacar(100)
    conta1.imprimirSaldo()
    conta1.sacar(50)
    conta1.imprimirSaldo()
    conta1.depositar(5000)
    conta1.imprimirSaldo()

    conta2 = Conta(199234, 'CHAPOLIM COLORADO', 20300, 3000.00)
    conta2.imprimirSaldo()
    conta2.sacar(155)
    conta2.imprimirSaldo()
    conta2.depositar(1500)
    conta2.imprimirSaldo()
