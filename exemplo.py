def imprime_listas(lista):
    for item in lista:
        print(item)

frutas = ["Banana", "Maça", "Pera", "Uva"]
carros = ["Gol", "Corsa", "Celta", "Chevette", "Fusca"]
tupla = (33, 44, 55, 66, 77, 88, 99, 00) 

imprime_listas(tupla)


pessoa = {
    "nome": "Pessoa",
    "Idade": 00,
    "Cidade": "Cidade"
}

def verifica_cidade(dicionario:dict):
    if dicionario["Cidade"] == "CG":
        return "É de Campo Grande"
    else:
        return f"É de {dicionario["Cidade"]}"

print(verifica_cidade(pessoa))
