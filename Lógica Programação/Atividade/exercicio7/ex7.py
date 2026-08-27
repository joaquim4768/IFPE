salario = float(input())

if salario > 1212:
    bonus = 1.15
else:
    bonus = 1.20

salarioReajustado = salario * bonus
print(f"R$ {salarioReajustado:.2f}")  