class Att01:
    def __init__(self, Nome,Idade,Endereco):
        self.nome = Nome
        self.idade = Idade
        self.endereco = Endereco

    def mostrarEndereco(self):
        return self.endereco
    
    def alterarEndereco(self,Endereco):
        self.endereco = Endereco
        return self.endereco
    
    
        