def calcularMediaValores(lista):
    if len(lista) == 0:
        return 0
    return sum(lista) / len(lista)


valores = [10, 20, 30, 40]
print(calcularMediaValores(valores))