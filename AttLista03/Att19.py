class Compra:
    def __init__(self, Numero, Produto, Valor):
        self.numero = Numero
        self.produto = Produto
        self.valor = Valor
        self.valorTotal = 0

    def getNumero(self):
        return self.numero

    def setNumero(self, Numero):
        self.numero = Numero

    def getProduto(self):
        return self.produto

    def setProduto(self, Produto):
        self.produto = Produto

    def getValor(self):
        return self.valor

    def setValor(self, Valor):
        self.valor = Valor

    def getValor_total(self):
        return self.valorTotal

    def setValor_total(self, ValorTotal):
        self.valorTotal = ValorTotal

    def calcularValorTotal(self):
        ICMS = self.valor * 0.17
        Frete = self.valor * 0.05
        self.valorTotal = self.valor + ICMS + Frete
        return self.valorTotal


class CompraAvista(Compra):
    def __init__(self, Numero, Produto, Valor, Desconto):
        super().__init__(Numero, Produto, Valor)
        self.desconto = Desconto

    def get_desconto(self):
        return self.desconto

    def set_desconto(self, Desconto):
        self.desconto = Desconto

    def calcularValorTotal(self):
        Total = super().calcularValorTotal()
        DescontoValor = Total * (self.desconto / 100)
        TotalFinal = Total - DescontoValor
        return TotalFinal


class CompraParcelada(Compra):
    def __init__(self, Numero, Produto, Valor, NumeroParcelas):
        super().__init__(Numero, Produto, Valor)
        self.numeroParcelas = NumeroParcelas

    def get_numero_parcelas(self):
        return self.numeroParcelas

    def set_numero_parcelas(self, NumeroParcelas):
        self.numeroParcelas = NumeroParcelas

    def calcularValorTotal(self):
        Total = super().calcularValorTotal()
        return Total

    def SimularNumeroDeParcelas(self):
        Total = self.calcularValorTotal()
        valorParcela = Total / self.numeroParcelas
        return valorParcela
