def dados_pessoa(**kwargs):
    print("Tipo de dado recebido:", type(kwargs))
    for chave, valor in kwargs.items():
        print(f"{chave.capitalize()} é {valor}")


dados_pessoa(
    nome="João",
    sobrenome="Silva",
    email="joaosilva@mail.com",
    pais="Brasil",
    idade=30,
    telefone="11987654321"
)