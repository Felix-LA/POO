class Ingresso:
    def __init__(self, Preco, Setor):
        self.preco = Preco
        self.setor = Setor

    def alterarPreco(self, NovoPreco):
       self.preco = NovoPreco 
    
    def getPreco(self):
        return self.preco

    def mostrarSetor(self):
        print(f'O setor em que voce comprou foi para o {self.setor}')

class IngressoVIP(Ingresso):
    def __init__(self, Preco, Setor, Camarote: bool = False, OpenBar: bool = False, OpenFood: bool = False):
        super().__init__(Preco, Setor)
        self.camarote = Camarote
        self.open_bar = OpenBar
        self.open_food = OpenFood

    def pegarBebida(self):
        if self.open_bar:
            print("Voce pegou a bebida!")
        print('voce nao pode acessar pois nao tem acesso mesmo com o VIP')

    def acessarCamarote(self):
        if self.camarote:
            print('Voce acessou o camarote meu cunpade')
        print('Voce nao tem permissao para acessar o camorote mesmo com o VIP')

    def mostrarDetalhes(self):
        print(f"Ingresso VIP - Setor: {self.setor}, Preço: R${self.getPreco()}")
        print(f"Open Bar: {'Sim' if self.open_bar else 'Não'}")
        print(f"Open Food: {'Sim' if self.open_food else 'Não'}")
        print(f"Camarote: {'Sim' if self.camarote else 'Não'}")
