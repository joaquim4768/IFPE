saldoMedio = float(input())
valorCredito = 0

if saldoMedio > 400:
    valorCredito = (30/100) * saldoMedio
elif saldoMedio > 300:
    valorCredito = (25/100) * saldoMedio
elif saldoMedio > 200:
    valorCredito = (20/100) * saldoMedio
else:
    valorCredito = (10/100) * saldoMedio

print(f"R$ {valorCredito:.2f}")