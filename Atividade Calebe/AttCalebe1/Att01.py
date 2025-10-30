class Aluno:
    def __init__(self,Nome,Matricula):
        self.nome = Nome
        self.matricula = Matricula

    def exibirNome(self):
        print(f"Aluno: {self.nome}")
    
aluno = Aluno("daasdpias", "hadoihoisa")
aluno.exibirNome()
        