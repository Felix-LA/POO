class Triangulo:
    def __init__(self,LadoA,LadoB,LadoC):
        self.ladoA = LadoA
        self.ladoB = LadoB
        self.ladoC = LadoC
    
    def calcularPerimetro(self):
        return f"A soma do perimetro é: " + str(self.ladoA + self.ladoB + self.ladoC)

    def getMaiorLado(self):
        return f"O maior lados dos três é: " + str(max([self.ladoA, self.ladoB, self.ladoC]))

        