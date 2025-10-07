class Conta:
    def __init__(self,Nome,Cpf,Numero,Saldo):
        self.nome = Nome
        self.cpf = Cpf
        self.numero = Numero
        self.saldo = Saldo

    def depositar(self,valor):
        self.saldo = self.saldo + valor
        return f"Saldo Atualizado"
    
    def sacar(self,valor):
        if valor <= self.saldo:
            return F"Valor Sacado com Sucesso"
        else:
            return f"Saldo Insuficiente"
        
    def imprimirSaldo(self):
        return f"O saldo Atual é: {self.saldo}"
    
    
        