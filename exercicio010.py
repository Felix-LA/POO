def financiamento(valorVeiculo,ValorEntrada,TaxaJuros,QuantidadeParcelas):
    valorAPagar = valorVeiculo - ValorEntrada
    juros = TaxaJuros / 100
    valorTotal = valorAPagar * ((1 + juros) ** QuantidadeParcelas)

    valorParcela = valorTotal / QuantidadeParcelas
    jurosPagos = valorTotal - valorAPagar


    return print(f"Valor financiado: R$ {valorAPagar:.2f}"
                 "\n"
                 f"Total a pagar: R$ {valorTotal:.2f}"
                 "\n"
                 f"Juros pagos: R$ {jurosPagos:.2f}"
                 "\n"
                 f"Valor de cada parcela ({QuantidadeParcelas}x): R$ {valorParcela:.2f}"
                 )




financiamento(50000,10000,2,24)

















    # for i in range (QuantidadeParcelas):
    #     juros = (1 + juros) ** i
    # valorparcela = (montante * juros) / QuantidadeParcelas
    # valorTotal = montante * juros
    # jurosPagos = valorTotal - montante
    # return jurosPagos,valorparcela,valorTotal
    



# montante = 1000
# TaxaJuros = 0.010
# QuantidadeParcelas = 36

# a = ((1 + TaxaJuros) ** QuantidadeParcelas)
# jurosComposto = montante * a
# print(f"{a:.2f}")
# print(f"{jurosComposto:.2f}")