def Conta(dia, **kwargs):
    valor = kwargs.get("valor", 0)
    taxa = kwargs.get("taxa", 0)
    couvert = kwargs.get("couvert", 0)

    
    descontos = {
        "terça-feira": 0.10,
        "quarta-feira": 0.15,
        "quinta-feira": 0.20
    }

    descontoDia = descontos.get(dia.lower(), 0)
    valorComDesconto = valor * (1 - descontoDia)

    taxaServico = valorComDesconto * taxa
    total = valorComDesconto + taxaServico + couvert

    print(f"Conta S/ Taxas: {valorComDesconto:.2f}")
    print(f"Conta C/ Taxas: {total:.2f}")
    print(f"Rodízio: {valorComDesconto:.2f}")
    print(f"Taxa Serviço: {taxaServico:.2f}")
    print(f"Couvert: {couvert}")
    print(f"TOTAL R$: {total:.2f}")





Conta("quinta-feira", valor = 99.90, taxa = 0.10, couvert = 15)