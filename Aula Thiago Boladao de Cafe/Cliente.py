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
    
    def buscarPorID(self,ID):
        self.db = Database()
        dados = self.db.select_by_id(ID)
        return dados

    def update(self,id,dados):
        self.db = Database()
        dadosAtualizados = self.db.update(id,dados)
        return dadosAtualizados

    def excluir(self,id):
        self.db = Database()
        result = self.db.delete(id)
        return result

    
        