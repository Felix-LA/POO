class Filme:
    def __init__(self, Nome, duracao):
        self.nome = Nome
        self.duracao = duracao

    def play(self):
        print(f"O filme {self.nome}, esta comecando, e tem duracao de {self.duracao}")

class Acao(Filme):
    def __init__(self, Nome, Duracao):
        super().__init__(Nome, Duracao)
        
    def explodir(self):
        print("Boooooommm!")

class Drama(Filme):
    def __init__(self, Nome, Duracao):
        super().__init__(Nome, Duracao)
       
    def romantico(self):
        print("Melancolico!")

class Suspense(Filme):
    def __init__(self, Nome, Duracao):
        super().__init__(Nome, Duracao)
       
    def medo(self):
        print("tantantannnnnnn!")
