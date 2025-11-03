class Att08:
    def __init__(self, numero, nome, saldo=0.0):
        self.numero = numero
        self.nome = nome
        self.saldo = saldo

    def alterarNome(self, novo_nome):
        self.nome = novo_nome

    def deposito(self, valor):
        if valor > 0:
            self.saldo += valor
        else:
            print("Valor de depósito inválido.")

    def saque(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saque inválido — saldo insuficiente ou valor negativo.")

    def exibir_dados(self):
        print(f"Conta: {self.numero} | Correntista: {self.nome} | Saldo: R${self.saldo:.2f}")


# Exemplo de uso:
c1 = Att08(101, "Maria", 500)
c1.exibir_dados()
c1.deposito(200)
c1.saque(100)
c1.exibir_dados()