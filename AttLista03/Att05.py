class Circulo:
    def __init__(self,Raio):
        self.raio = Raio

    def imprimirValorRaio(self):
        return f"O valor do Raio é: {self.raio}"
    
    def calcularAreaCirculo(self):
        area = 3.14 * (self.raio * self.raio)
        return f"A area do circulo é: {area}"
    
    def calcularCircuferenciaCirculo(self):
        circuferencia = 2 * 3.14 * self.raio
        return f"A circuferencia do circulo é: {circuferencia}"
    
circulo = Circulo(6)

print(circulo.imprimirValorRaio())
print(circulo.calcularAreaCirculo())
print(circulo.calcularCircuferenciaCirculo())
      