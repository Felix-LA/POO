class Dog:
    def __init__(self,Nome,Peso, COR):
        self.nome = Nome
        self.peso = Peso
        self.cor = COR

    def latir(self):
        return f"{self.nome} Au AU AU"
    
    def comer(self):
        return f"{self.nome} Comendo..."
    
dog1 = Dog("Morgana", 4.5, "Preto")
print("Peso da Morgana: ", dog1.peso)
print(dog1.comer())
        