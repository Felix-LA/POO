class Att09:
    def __init__(self, p, q):
        if q == 0:
            print("Erro: o denominador não pode ser zero!")
            
        self.p = p
        self.q = q
        self.simplificar()

    def __repr__(self):
        return f"{self.p}/{self.q}"

    def simplificar(self):
        # simplifica o racional dividindo pelo MDC
        from math import gcd
        divisor = gcd(self.p, self.q)
        self.p //= divisor
        self.q //= divisor

    def inverter_sinal(self):
        return Att09(-self.p, self.q)

    def somar(self, outro):
        return Att09(self.p * outro.q + outro.p * self.q, self.q * outro.q)

    def subtrair(self, outro):
        return Att09(self.p * outro.q - outro.p * self.q, self.q * outro.q)

    def produto(self, outro):
        return Att09(self.p * outro.p, self.q * outro.q)

    def quociente(self, outro):
        if outro.p == 0:
            raise ZeroDivisionError("Divisão por racional com numerador zero.")
        return Att09(self.p * outro.q, self.q * outro.p)


# Exemplo de uso:
r1 = Att09(2, 3)
r2 = Att09(3, 4)

print("r1 =", r1)
print("r2 =", r2)
print("Soma =", r1.somar(r2))
print("Subtração =", r1.subtrair(r2))
print("Produto =", r1.produto(r2))
print("Quociente =", r1.quociente(r2))
print("Inversão de sinal r1 =", r1.inverter_sinal())