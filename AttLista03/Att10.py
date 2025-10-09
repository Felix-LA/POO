class NotaFiscal:
    def __init__(self, Numero, Tipo, Serie, CNPJ, RazaoSocial, Data, ValorProdutos, ICMS, Frete, IPI):
        self.numero = Numero
        self.tipo = Tipo
        self.serie = Serie
        self.cnpj = CNPJ
        self.razaoSocial = RazaoSocial
        self.data = Data
        self.valorProdutos = ValorProdutos
        self.icms = ICMS
        self.frete = Frete
        self.ipi = IPI
        self.valorTotal = 0

    def obterNumero(self):
        return self.numero

    def obterDataEmissao(self):
        return self.data

    def alterarRazaoSocial(self, nova_razao):
        self.razaoSocial = nova_razao

    def calcularValorTotal(self):
        self.valorTotal = self.valorProdutos + self.frete + self.icms + self.ipi
        return self.valorTotal