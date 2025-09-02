def financiamento(valorVeiculo,ValorEntrada,TaxaJuros,QuantidadeParcelas):
    valorAPagar = valorVeiculo - ValorEntrada
    juros = TaxaJuros / 100
    jurosComposto = valorAPagar * ((1 + juros) ** QuantidadeParcelas)
    print(jurosComposto)

    valorParcela = (valorAPagar + jurosComposto) / QuantidadeParcelas
    valorTotal = valorAPagar + jurosComposto
    jurosPagos = valorTotal - valorAPagar
    return valorParcela,jurosPagos,valorTotal














    # for i in range (QuantidadeParcelas):
    #     juros = (1 + juros) ** i
    # valorparcela = (montante * juros) / QuantidadeParcelas
    # valorTotal = montante * juros
    # jurosPagos = valorTotal - montante
    # return jurosPagos,valorparcela,valorTotal
    

print(financiamento(100000,40000,1,36))


# montante = 1000
# TaxaJuros = 0.010
# QuantidadeParcelas = 36

# a = ((1 + TaxaJuros) ** QuantidadeParcelas)
# jurosComposto = montante * a
# print(f"{a:.2f}")
# print(f"{jurosComposto:.2f}")