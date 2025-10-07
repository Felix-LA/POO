class Funcionario:
    def __init__(self,nome,login,senha):
        self.nome = nome
        self.login = login
        self.senha = senha

    def logar(self):
        return f"{self.nome} Logado com Sucesso!!!"
    
    def alterar_senha(self,novaSenha):
        self.senha = novaSenha
        return f"Senha Alterada com Sucesso!!!"
    

class Gerente(Funcionario):
    def __init__(self, nome, login, senha,setor):
        super().__init__(nome, login, senha)
        self.setor = setor
        