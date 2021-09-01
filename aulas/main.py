from aulas.conta import Conta

if __name__ == '__main__':
    conta1 = Conta(199249, 'ELIEZER ALVES', 250, 5000.00)
    conta1.imprimirSaldo()
    conta1.sacar(100)
    conta1.imprimirSaldo()
    conta1.sacar(50)
    conta1.imprimirSaldo()
    conta1.depositar(5000)
    conta1.imprimirSaldo()

    conta2 = Conta(199234, 'CHAPOLIM COLORIDO', 20300, 3000.00)
    conta2.imprimirSaldo()
    conta2.sacar(155)
    conta2.imprimirSaldo()
    conta2.depositar(1500)
    conta2.imprimirSaldo()

    # manipulação do limite da conta 2
    print("O limite da conta é {}".format(conta2.getLimite()))
    conta2.setLimite(5000)
    print("O limite da conta é {}".format(conta2.getLimite()))

    # manipulação do titular da conta 2
    print("O titular da conta é {}".format(conta2.getTitular()))
    conta2.setTitular('CHAPOLIN COLORADO')
    print("O titular da conta é {}".format(conta2.getTitular()))

    # acessando as properties do objeto
    print(conta2.limite)
    conta2.limite = 8500
    print(conta2.limite)
    print(conta2.saldo)

    # acessando os métodos estáticos da classe
    print("Código do banco: {}".format(Conta.codigBanco()))
