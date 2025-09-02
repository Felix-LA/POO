def somaImposto(taxaImposto,Custo):
    custoFinal = ((taxaImposto / 100) * Custo) + Custo
    return custoFinal

print(somaImposto(15, 100))