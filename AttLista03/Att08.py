class AlunoAcademia:
    def __init__(self, Nome, Idade, Peso, Altura, Mensalidade=120.0):
        self.nome = Nome
        self.idade = Idade
        self.peso = Peso
        self.altura = Altura
        self.mensalidade = Mensalidade

    def calcularImc(self):
        imc = self.peso / (self.altura ** 2)
        return round(imc, 2)

    def obterValorMensalidade(self):
        if self.idade < 18:
            return round(self.mensalidade * 0.9, 2)
        return self.mensalidade
