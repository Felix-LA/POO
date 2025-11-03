import math

class Att06:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vetor3D({self.x}, {self.y}, {self.z})"

    def soma(self, outro):
        return Att06(self.x + outro.x, self.y + outro.y, self.z + outro.z)

    def subtracao(self, outro):
        return Att06(self.x - outro.x, self.y - outro.y, self.z - outro.z)

    def produtoEscalar(self, outro):
        return self.x * outro.x + self.y * outro.y + self.z * outro.z

    def produtoVetorial(self, outro):
        x = self.y * outro.z - self.z * outro.y
        y = self.z * outro.x - self.x * outro.z
        z = self.x * outro.y - self.y * outro.x
        return Att06(x, y, z)

    def modulo(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)