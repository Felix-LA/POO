class Brinquedo:
    def __init__(self, Nome, Cor, Tamanho, Preco):
        self.nome = Nome
        self.cor = Cor
        self.tamanho = Tamanho
        self.preco = Preco

    def brincar(self):
        print(f'Estou brincando com o {self.nome}')


class MaxStill(Brinquedo):
    def brincar(self):
        print(f"Entrando no Modo Turbo")

class BuzzLight(Brinquedo):
    def brincar(self):
        print(f"AO Infinito e ALEMMMM!!!")

class RelampagoMarkin(Brinquedo):
    def brincar(self):
        print(f"KATCHUMMMMM")

class SeiyaDePegasus(Brinquedo):
    def brincar(self):
        print(f"Meteoro de Pégasus")

class SalsichoScoobydoo(Brinquedo):
    def brincar(self):
        print(f'Scoobyy meu filho!')

