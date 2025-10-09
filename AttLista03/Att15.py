class Passagem:
    def __init__(self, preco, assento):
        self.preco = preco
        self.assento = assento

    def alterar_preco(self, PrecoNovo):
        self.preco = PrecoNovo

    def escolher_assento(self):
        print(f'Voce sentou no assento {self.assento}')

class PassagemOnibus(Passagem):
    def __init__(self, Preco, Assento, Placa, LeitoPar):
        super().__init__(Preco, Assento)
        self.placa = Placa
        self.leito_par = LeitoPar

    def sair(self):
        print(f'O onibus esta saindo')
    
    def abastecer(self):
        print(f'O onibus com a placa {self.placa} esta abastecendo.')


class PassagemAviao(Passagem):
    def __init__(self, Preco, Assento, PortaoDeEmbarque, CheckIn):
        super().__init__(Preco, Assento)
        self.portaodeembarque = PortaoDeEmbarque
        self.checkin = CheckIn

    def decolar(self):
        print(f'O aviao esta decolando!')
    
    def abastecer(self):
        print(f'O aviao esta abastecendo neste exato momento!')