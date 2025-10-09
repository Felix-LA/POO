class Carro:
    def __init__(self, Modelo, Marca, Cor, Ano, Valor, Nivel=5, Consumo=0.0):
        self.modelo = Modelo
        self.marca = Marca
        self.cor = Cor
        self.ano = Ano
        self.valor = Valor
        self.nivel = Nivel
        self.consumo = Consumo
        self.ligado = False

    def ligar(self):
        self.ligado = True
        print(f"{self.modelo} ligado!")

    def abastecer(self, litros):
        self.nivel += litros
        print(f"Abastecido com {litros} litros. Nível atual: {self.nivel}L")

    def andar(self, km):
        if not self.ligado:
            print("O carro precisa estar ligado para andar!")
            return
        gasto = km * self.consumo
        if gasto > self.nivel:
            print("Combustível insuficiente para percorrer essa distância!")
        else:
            self.nivel -= gasto
            print(f"Andou {km} km. Nível de combustível restante: {self.nivel}L")

    def verificarNivel(self):
        print(f"Nível atual de combustível: {self.nivel}L")
        return self.nivel

    def calcularImposto(self):
        ipva = self.valor * 0.025
        return round(ipva, 2)