class Estudante:
    def __init__(self,nome,idade,nota): ## Método Construtor
        self.nome = nome
        self.idade = idade
        self.nota = nota

    def get_grade(self):
        return self.nota
        



        
e1 = Estudante("Luis",20,10)
e2 = Estudante("Jow",22,10)


print(e1.nome,e1.idade,e1.nota)
print(e2.nome,e2.idade,e2.nota)
print(e1.get_grade())