class Att07:
    def __init__(self, marca, ano, preco):
        self.marca = marca
        self.ano = ano
        self.preco = preco

    def mostrarPreco(self):
        return self.preco

    def exibirDados(self):
        print(f"Marca: {self.marca}, Ano: {self.ano}, Preço: R${self.preco:.2f}")


# Criação da lista de carros
carros = []

for i in range(5):
    print(f"\nCarro {i+1}:")
    marca = input("Digite a marca: ")
    ano = int(input("Digite o ano: "))
    preco = float(input("Digite o preço: "))
    carros.append(Att07(marca, ano, preco))

# Lê o valor p
p = float(input("\nDigite o valor limite de preço (p): "))

print(f"\nCarros com preço menor que R${p:.2f}:")
for carro in carros:
    if carro.mostrar_preco() < p:
        carro.exibir_dados()