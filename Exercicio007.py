def calculoSalario(horasTrabalhadas,salario):
    if horasTrabalhadas <= 40:
        return horasTrabalhadas * salario
    else:
        horasExtra = horasTrabalhadas - 40
        bonus = (salario / 2) * horasExtra
        return (horasTrabalhadas * salario) + bonus
    
print(calculoSalario(41,2))