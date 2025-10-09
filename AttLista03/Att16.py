class Funcionario:
    def __init__(self, Nome, Matricula, Salario):
        self.nome = Nome
        self.matricula = Matricula
        self.salario = Salario
        self.pontosBatidos = []

    def bater_ponto(self, Ponto):
        self.pontosBatidos.append(1)
        print('voce acabou de bater o ponto')
        
        if Ponto in [0, 1]:
            self.pontosBatidos.append(Ponto)
            print(f"Ponto registrado para o {self.nome}: {Ponto}")
            return 
        print("Erro de Digitação")
    def __str__(self):
        return f"Nome: {self.nome}, Matrícula: {self.matricula}, Salário: R${self.salario:.2f}"


class Vendedor(Funcionario):
    def __init__(self, Nome, Matricula, Salario, Comissao):
        super().__init__(Nome, Matricula, Salario)
        self.comissao = Comissao

    def baterMeta(self, Vendas):
        if Vendas >= 5000:
            self.bonus = self.salario * (self.comissao / 100)
            print("Meta de {self.nome} Atingida.\n Bonus de {self.bonus:.2f}")
            return

        print("Meta não atingida")

class Gerente(Funcionario):
    def __init__(self, Nome, Matricula, Salario, Senha):
        super().__init__(Nome, Matricula, Salario)
        self.senha = Senha
        
    def aprovarPagamento(self, Senha):
        if Senha == self.senha:
            print("Pagamento Aprovado")
            return
        print('senha incorreta...')