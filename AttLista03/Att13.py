class Pessoa:
    def __init__(self, Nome, Telefone, Email, Endereco):
        self.nome = Nome
        self.telefone = Telefone
        self.email = Email
        self.endereco = Endereco

    def negociar(self):
        print(f"{self.nome} está negociando...")


class Fisica(Pessoa):
    def __init__(self, Nome, Telefone, Email, Endereco, CPF):
        super().__init__(Nome, Telefone, Email, Endereco)
        self.cpf = CPF

    def mostrar_dados(self):
        print("=== Pessoa Física ===")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")
        print(f"Endereço: {self.endereco}")
        print(f"CPF: {self.cpf}")

    def registrar_em(self, Lugar):
        print(f"O CPF ({self.cpf}) foi registrado em {Lugar}.")


class Juridica(Pessoa):
    def __init__(self, Nome, Telefone, Email, Endereco, CNPJ):
        super().__init__(Nome, Telefone, Email, Endereco)
        self.cnpj = CNPJ

    def mostrar_dados(self):
        print("=== Pessoa Jurídica ===")
        print(f"Nome: {self.nome}")
        print(f"Telefone: {self.telefone}")
        print(f"Email: {self.email}")
        print(f"Endereço: {self.endereco}")
        print(f"CNPJ: {self.cnpj}")

    def registrar_em(self, Lugar):
        print(f"O CNPJ ({self.cnpj}) foi registrado em {Lugar}.")
