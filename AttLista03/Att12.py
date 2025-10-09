class Pessoa:
    def __init__(self, Nome, Idade) :
        self.nome = Nome
        self.idade = Idade

class Aluno(Pessoa):
    def __init__(self, Nome, Idade, Notas):
        super().__init__(Nome, Idade)
        self.notas = Notas

    def mostrarNotas(self):
        for i in self.notas:
            print(f"Suas notas sao: {i}")

    def calcularMedia(self):
        media = sum(self.notas) / len(self.notas)
        print(f"A media do aluno {self.nome} é de {media}")

    def estudar(self):
        print("O aluno " + self.nome + ", esta estudando")

class Professor(Pessoa):
    def __init__(self, Nome, Idade, Formacao, Disciplina, CargaHoraria, Salario):
        super().__init__(Nome, Idade)
        self.formacao = Formacao
        self.disciplina = Disciplina
        self.carga_horaria = CargaHoraria
        self.salario = Salario
    
    def ensinar(self):
        print(f"O professor {self.nome}, esta ensinando {self.disciplina}")

    def aplicar_prova(self):
        print(f"O professor {self.nome}, aplicou uma prova de {self.disciplina}")

    def corrigir_provas(self):
        print(f"O professor {self.nome} esta corrigindo as provas")

    def receber_salario(self):
        print(f"O professor {self.nome} recebeu {self.salario} na sua conta.")
