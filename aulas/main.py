from conta import Conta, ContaCorrente, ContaPoupanca, ContaPoupancaEspecial, ListaContas

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

    print("________________________________________________________")

    #Herança
    contaCorrente = ContaCorrente(505050, "Eliezer Alves", 500.00, 1000.00)
    print(contaCorrente.getTitular())
    print(contaCorrente.getTaxaOperacao())
    contaCorrente.imprimirSaldo()
    contaCorrente.debitarTaxaOperacao(20.5)
    contaCorrente.imprimirSaldo()

    print("________________________________________________________")

    contaPoupanca = ContaPoupanca(707070, "Eliezer Alves", 1000.00, 10000.00)
    print(contaPoupanca.getTitular())
    print(contaPoupanca.getTaxaRendimento())
    contaPoupanca.imprimirSaldo()
    contaPoupanca.creditarRendimento()
    contaPoupanca.imprimirSaldo()
    # contaCorrente.imprimir()
    # contaPoupanca.imprimir()

    #Polimorfismo

    contas = [contaCorrente,contaPoupanca]

    # for c in contas:
    #     c.imprimir()

    print()
    print("________________________________________________________")
    print("____________________--AULA  7--_________________________")
    print("________________________________________________________")
    print()

    listaContas = ListaContas(contas)
    for c in listaContas:
        print(c)

    print()
    print("________________________________________________________")
    print("____________________--AULA  8--_________________________")
    print("________________________________________________________")
    print()

    print('A quantidade de itens na lista é {}'.format(len(listaContas)))
    for c in listaContas:
        print(c)

    del listaContas[1]

    print("Lista de contas após a remoção do item 1")
    for c in listaContas:
        print(c)

    listaContas.insert(contaPoupanca)
    print("Lista de contas após a insersão")
    for c in listaContas:
        print(c)

    contaPoupanca2 = ContaPoupanca(1111111, "Vladimir Putin", 9999999999999999999, 999999999999999999999)
    listaContas[1] = contaPoupanca2
    print("Lista de contas após a atualização")
    for c in listaContas:
        print(c)

    print()
    print("________________________________________________________")
    print("____________________--AULA  9--_________________________")
    print("________________________________________________________")
    print()

    contaPoupancaEspecial = ContaPoupancaEspecial(10101010, "Valeri Legasov", 15328372563, 1000000000000)

    print(contaPoupancaEspecial)
    contaPoupancaEspecial.imprimirSaldo()
    contaPoupancaEspecial.imprimir()