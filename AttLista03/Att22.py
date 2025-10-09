class Transporte:
    def __init__(self, Capacidade):
        self.capacidade = Capacidade

    def getCapacidade(self):
        return self.capacidade

    def setCapacidade(self, Capacidade):
        self.capacidade = Capacidade


class Terrestre(Transporte):
    def __init__(self, Capacidade, NumeroRodas):
        super().__init__(Capacidade)
        self.numeroRodas = NumeroRodas

    def getNumeroRodas(self):
        return self.numeroRodas

    def setNumeroRodas(self, NumeroRodas):
        self.numeroRodas = NumeroRodas


class Automovel(Terrestre):
    def __init__(self, Capacidade, NumeroRodas, Cor, NumeroPortas, Placa):
        super().__init__(Capacidade, NumeroRodas)
        self.cor = Cor
        self.numeroPortas = NumeroPortas
        self.placa = Placa

    def getCor(self):
        return self.cor

    def setCor(self, Cor):
        self.cor = Cor

    def getNumeroPortas(self):
        return self.numeroPortas

    def setNumeroPortas(self, Portas):
        self.numeroPortas = Portas

    def getPlaca(self):
        return self.placa

    def setPlaca(self, Placa):
        self.placa = Placa

    def exibir_info(self):
        print(f"Automóvel {self.cor}, {self.numeroPortas} portas, placa {self.placa}")

class Aquatico(Transporte):
    def __init__(self, Capacidade, Tipo):
        super().__init__(Capacidade)
        self.tipo = Tipo

    def getTipo(self):
        return self.tipo

    def setTipo(self, Tipo):
        self.tipo = Tipo


class Lancha(Aquatico):
    def __init__(self, Capacidade, Tipo, VelocidadeMax):
        super().__init__(Capacidade, Tipo)
        self.velocidadeMax = VelocidadeMax

    def getVelocidadeMax(self):
        return self.velocidadeMax

    def exibir_info(self):
        print(f"Lancha ({self.getTipo()}) - Capacidade: {self.getCapacidade()} - Velocidade Máx: {self.velocidadeMax} km/h")


class Navio(Aquatico):
    def __init__(self, Capacidade, Tipo, NumeroTripulantes):
        super().__init__(Capacidade, Tipo)
        self.NumeroTripulantes = NumeroTripulantes

    def getNumeroTripulantes(self):
        return self.NumeroTripulantes

    def exibir_info(self):
        print(f"Navio ({self.getTipo()}) - Capacidade: {self.getCapacidade()} - Tripulantes: {self.NumeroTripulantes}")


class Aereo(Transporte):
    def __init__(self, Capacidade, Tipo):
        super().__init__(Capacidade)
        self.tipo = Tipo

    def getTipo(self):
        return self.tipo

    def setTipo(self, Tipo):
        self.tipo = Tipo


class AviaoMonomotor(Aereo):
    def __init__(self, Capacidade, Tipo, Autonomia):
        super().__init__(Capacidade, Tipo)
        self.autonomia = Autonomia

    def exibir_info(self):
        print(f"Avião Monomotor ({self.getTipo()}) - Capacidade: {self.getCapacidade()} - Autonomia: {self.autonomia} km")


class AviaoComercial(Aereo):
    def __init__(self, Capacidade, Tipo, Empresa):
        super().__init__(Capacidade, Tipo)
        self.empresa = Empresa

    def exibir_info(self):
        print(f"Avião Comercial ({self.getTipo()}) - Empresa: {self.empresa} - Capacidade: {self.getCapacidade()} passageiros")
