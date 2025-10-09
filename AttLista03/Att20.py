class Pessoa:
    def __init__(self, nome, CPF):
        self.nome = nome
        self.cpf = CPF


class ContaBancaria:
    def __init__(self, Numero, Titular: Pessoa, Saldo=0.0):
        self.numero = Numero
        self.titular = Titular
        self.saldo = Saldo

    def depositar(self, Valor):
        print(f"Depositando R${Valor:.2f} na conta de {self.titular.nome}")
        self.saldo += Valor
        print(f"Novo saldo: R${self.saldo:.2f}")

    def sacar(self, Valor):
        if Valor <= self.saldo:
            self.saldo -= Valor
            print(f"Saque de R${Valor:.2f} realizado com sucesso!")
        else:
            print(f"Saldo insuficiente, Favor trabalhar mais")

    def obter_saldo(self):
        return self.saldo


class ContaCorrente(ContaBancaria):
    def __init__(self, Numero, Titular: Pessoa, Saldo=0.0, Limite=500.0):
        super().__init__(Numero, Titular, Saldo)
        self.limite = Limite

    def sacar(self, Valor):
        if Valor <= self.saldo + self.limite:
            self.saldo -= Valor
            print(f"Saque de R${Valor:.2f} realizado com sucesso (conta corrente)!")
        else:
            print(f"Saldo insuficiente, Favor trabalhar mais")


class ContaPoupanca(ContaBancaria):
    def __init__(self, Numero, Titular: Pessoa, Saldo=0.0, TaxaJuros=0.015):
        super().__init__(Numero, Titular, Saldo)
        self.taxaJuros = TaxaJuros

    def aplicar_juros(self):
        juros = self.saldo * self.taxaJuros
        self.saldo += juros
        print(f"Juros de R${juros:.2f} aplicados! Novo saldo: R${self.saldo:.2f}")


class ContaFundoInvestimento(ContaBancaria):
    def __init__(self, Numero, Titular: Pessoa, Saldo=0.0, RendimentoMensal=0.03):
        super().__init__(Numero, Titular, Saldo)
        self.rendimentoMensal = RendimentoMensal

    def aplicarRendimento(self):
        rendimento = self.saldo * self.rendimentoMensal
        self.saldo += rendimento
        print(f"Rendimento de R${rendimento:.2f} aplicado! Novo saldo: R${self.saldo:.2f}")
