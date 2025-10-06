def calcularMultaPeixe(peso):
    if peso > 50:
        excesso = peso - 50
        multa = excesso * 4.00
        return print(f"O excesso é: ", excesso, "\n" "A multa é: ", multa)
    else:
        return print("Sem Multa")
    
calcularMultaPeixe(55)
    