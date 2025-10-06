class Pessoa:
    def __init__(self,Nome,CPF,Fone,Email,Cidade,Estado):
        self.nome = Nome
        self.cpf = CPF
        self.fone = Fone
        self.email = Email
        self.cidade = Cidade
        self.estado = Estado

    
    def mostrarRegistro(self):
        return f'''Dados: 
        Nome: {self.nome}
        CPF: {self.cpf}
        Fone: {self.fone}
        Email: {self.email}
        Cidade: {self.cidade}
        Estado: {self.estado}
        '''
    
pessoa1 = Pessoa("Felix", 13423432, 12312321321,"adadasdasd","Campo Grande", "Mato Grosso do Sul")

print(pessoa1.mostrarRegistro())
        

