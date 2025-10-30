from DatabaseCliente import Database

class Cliente:
    def __init__(self, Nome=None,Cpf=None,Fone=None,Cidade=None):
        self.nome = Nome
        self.cpf = Cpf
        self.fone = Fone
        self.cidade = Cidade

    def cadastrar(self):
        self.db = Database()
        tupla = (self.nome,self.cpf,self.fone,self.cidade)
        result = self.db.insert(tupla)
        return result

    def buscar(self):
        self.db = Database()
        dados = self.db.select()
        return dados
        