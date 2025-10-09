class Imovel:
    def __init__(self, InscricaoMunicipal, IPTU):
        self.inscricaoMunicipal = InscricaoMunicipal
        self.valorAluguel = 0
        self.iptu = IPTU

    def obter_parcela_IPTU(self):
        print(f"\nIPTU total: R${self.iptu:.2f}")
        print("Parcelas em 12x:")
        for i in range(1, 13):
            parcela = self.iptu / 12
            print(f"Parcela {i}: R${parcela:.2f}")

    def setValorAluguel(self, Aluguel):
        self.valorAluguel = Aluguel


class Casa(Imovel):
    def __init__(self, InscricaoMunicipal, IPTU):
        super().__init__(InscricaoMunicipal, IPTU)

    def sala_estar(self):
        print("A casa tem exatamente 50x40x120 metros.")


class Apartamento(Imovel):
    def __init__(self, InscricaoMunicipal, IPTU):
        super().__init__(InscricaoMunicipal, IPTU)
        self.locais = ["Piscina", "Suíte"]

    def area_lazer(self):
        print("\nÁrea de lazer:")
        for i in self.locais:
            print(f"- {i}")


class Terreno(Imovel):
    def __init__(self, InscricaoMunicipal, IPTU):
        super().__init__(InscricaoMunicipal, IPTU)

    def obter_parcela_IPTU(self):
        print(f"\nIPTU total: R${self.iptu:.2f}")
        print("Parcelas em 87x:")
        for i in range(1, 88):
            parcela = self.iptu / 87
            print(f"Parcela {i}: R${parcela:.2f}")


class Chacara(Imovel):
    def __init__(self, InscricaoMunicipal, IPTU):
        super().__init__(InscricaoMunicipal, IPTU)

    def descricao(self):
        print("A chácara possui área verde, casa principal e espaço para eventos.")
