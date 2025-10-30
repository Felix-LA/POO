class Att02:
    def __init__(self,Nome,NumeroDeMatricula,Curso):
        self.nome = Nome
        self.numeroDeMatricula = NumeroDeMatricula
        self.curso = Curso

    def mostrarCurso(self):
        return self.curso
    
    def alterarCurso(self,NovoCurso):
        self.curso = NovoCurso
        return self.curso
        