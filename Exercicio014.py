def calcularConsumo(potenciaWatts, tempoHoras):
    consumo = (potenciaWatts / 1000) * tempoHoras
    return consumo


def calcular_conta(consumo, valorKwh):
    return consumo * valorKwh


potencia = 2000
tempo = 3
valor_kwh = 0.85

consumo = calcularConsumo(potencia, tempo)
conta = calcular_conta(consumo, valor_kwh)

print(f"Consumo: {consumo:.2f} kWh")
print(f"Valor da conta: R$ {conta:.2f}")