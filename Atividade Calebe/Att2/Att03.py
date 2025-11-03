class Att03:
    alunos = []

    def __init__(self,Matricula,Nome,NotaProva1,NotaProva2,NotaProva3):
        self.matricula = Matricula
        self.nome = Nome
        self.notaProva1 = NotaProva1
        self.notaProva2 = NotaProva2
        self.notaProva3 = NotaProva3
        self.media = (NotaProva1 + NotaProva2 + NotaProva3) / 3

        # Att03.alunos.append(self.nome, self.media)



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
    
    def aprovacao(self,Nome):
        if self.media >= 6:
            return f"Aluno Aprovado"
        else:
            return f"Aluno Reprovado"



def maiorMedia(alunos):
    maiorMedia = 0
    for i in alunos.values():
        if i >= maiorMedia:
            maiorMedia = i
    return maiorMedia


def menorMedia(alunos):
    menorMedia = list(alunos.values())[0]
    for i in alunos.values():
        if i <= menorMedia:
            menorMedia = i
    return menorMedia


# a1 = Att03(1, "Flka", 5, 7, 9)
# a2 = Att03(2, "Pedro", 5, 6, 7)
# b1 = Att03(3, "João", 7, 8, 9)
# b2 = Att03(4, "Maria", 9, 9, 9)

# a = [a1.media, a2.media, b1.media, b2.media]
# lista_aluno_media = {}

# for i in range(4):
#     lista_aluno_media[i] = a[i]
# buscarMaior = Att03.buscarAluno()
# print("Maior média:", maiorMedia(lista_aluno_media))
# print("Menor média:", menorMedia(lista_aluno_media))





        

    