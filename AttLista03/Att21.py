class Transporte:
    def __init__(self, Capacidade):
        self.capacidade = Capacidade
    
    def getCapacidade(self):
        return self.capacidade

    def setCapacidade(self, Valor):
        self.capacidade = Valor


class Aquatico(Transporte):
    def __init__(self, Capacidade, Tipo):
        super().__init__(Capacidade)
        self.tipo = Tipo


    def getTipo(self):
        return self.tipo

    def setTipo(self, Valor):
        self.tipo = Valor


class Automovel(Transporte):
    def __init__(self, Capacidade, NumeroRodas, NumeroPortas, Cor, Placa):
        super().__init__(Capacidade)
        self.numeroRodas = NumeroRodas
        self.numeroPortas = NumeroPortas
        self.cor = Cor
        self.placa = Placa

    def getNumeroRodas(self):
        return self.numeroRodas

    def setNumeroRodas(self, Numero):
        self.numeroRodas = Numero

    def getNumeroPortas(self):
        return self.numeroPortas

    def setNumeroPortas(self, Numero):
        self.numeroPortas = Numero

    def getCor(self):
        return self.cor

    def setCor(self, Valor):
        self.cor = Valor

    def getPlaca(self):
        return self.placa

    def setPlaca(self, Valor):
        self.placa = Valor


class Aereo(Transporte):
    def __init__(self, Capacidade, Tipo):
        super().__init__(Capacidade)
        self.tipo = Tipo

    def getTipo(self):
        return self.tipo

    def setTipo(self, Valor):
        self.tipo = Valor
