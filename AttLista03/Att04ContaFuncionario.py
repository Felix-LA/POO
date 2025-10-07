class ContaFuncionario:
    def __init__(self,Nome,Sobrenome,HorasTrabalhadas,ValorHora):
        self.nome = Nome
        self.sobrenome = Sobrenome
        self.horasTrabalhadas = HorasTrabalhadas
        self.valorHora = ValorHora

    def nomeCompleto(self):
        return f"{self.nome} {self.sobrenome}"
    
    def calcularSalario(self):
        salario = self.horasTrabalhadas * self.valorHora
        return f"Salario: {salario}"
    
    def incrementarHora(self, HoraAdicional):
        self.horasTrabalhadas += HoraAdicional
        return f"Horas Incrementadas com Sucesso"
    
        