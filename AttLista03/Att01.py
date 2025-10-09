class Pessoa:
    def __init__(self, Nome,Idade,Endereco):
        self.nome = Nome
        self.idade = Idade
        self.endereco = Endereco

    def mostrarNome(self):
        return f"Nome: {self.nome}"
    
    def alterarIdade(self,NovaIdade):
        self.idade = NovaIdade
        return f"A Nova Idade é: {self.idade}"
    
    def imprimirEndereco(self):
        return f"O Endereço é: {self.endereco}"
