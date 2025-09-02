def calcularTempo(Minutos):

    tempo = Minutos / 60
    if Minutos < 15:
        return print(f"Tempo: {tempo:.2f} horas")
    else:

        precoEstacionamento = 9 + (1.50 * (tempo - 1))
        pis = precoEstacionamento * 0.033
        cofins = precoEstacionamento * 0.020
        icms = precoEstacionamento * 0.17
        imposto = pis + cofins + icms

        total =  precoEstacionamento + imposto 

        return print(f"Tempo: {tempo:.2f} horas",
                     "\n",
                     f"PIS R$ {pis:.2f}"
                     "\n",
                     f"COFINS R$ {cofins:.2f}"
                     "\n",
                     f"ICMS R$ {icms:.2f}"
                     "\n",
                     f"IMPOSTO R$ {imposto:.2f}"
                     "\n",
                     f"TOTAL: R$ {total:.2f}")
    
calcularTempo(240)
