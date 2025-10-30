class Att03:
    alunos = []

    def __init__(self,Matricula,Nome,NotaProva1,NotaProva2,NotaProva3):
        self.matricula = Matricula
        self.nome = Nome
        self.notaProva1 = NotaProva1
        self.notaProva2 = NotaProva2
        self.notaProva3 = NotaProva3
        self.media = (NotaProva1 + NotaProva2 + NotaProva3) / 3

        Att03.alunos.append(self)



    def buscarAluno(self,Nome):
        if self.nome.lower() == Nome.lower():
            return f"Aluno: {self.nome}\n Media: {self.media}"
        else:
            return f"Aluno {Nome} nao encontrado"
        
    
    def verificarMedia(self,Nome):
        if self.nome == Nome:
            return self.media
        else:
            return f"Aluno {Nome} nao encontrado"
        
    def pegarMedia(self, aluno):
        return aluno.media
    

    def maiorMedia(self):
        maiorMedia = max(self.alunos, key= Att03.pegarMedia)
        return maiorMedia
    
    def menorMedia(self):
        menorMedia = min(self.alunos, key= Att03.pegarMedia)
        return menorMedia
    




        

    