class Aluno:
    def __init__(self,Nome,RA,Nota1,Nota2,Nota3,Nota4):
        self.nome = Nome
        self.ra = RA
        self.nota1 = Nota1
        self.nota2 = Nota2
        self.nota3 = Nota3
        self.nota4 = Nota4

    def mostrarSituacao(self):
        media = (self.nota1 + self.nota2 + self.nota3 + self.nota4) / 4
        if media >= 7:
            return f"Aluno {self.nome} Aprovado!!! \n Média: {media}"
        elif media <7 and media >= 5:
            return f"Aluno {self.nome} de Exame \n Média: {media}"        
        else:
            return f"Aluno {self.nome} Reprovado \n Média: {media}"
        

aluno = Aluno("fssfdsdf",23423423,7,9,5,8)
print(aluno.mostrarSituacao())