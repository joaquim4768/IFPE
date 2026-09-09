custoFabrica = float(input())
distribuidorP = 0
impostosP = 0
preço = 0

if custoFabrica > 70000:
    distribuidorP = (15/100) * custoFabrica
    impostosP = (20/100) * custoFabrica
    preço = custoFabrica + distribuidorP + impostosP
elif custoFabrica >= 35000:
    distribuidorP = (10/100) * custoFabrica
    impostosP = (15/100) * custoFabrica
    preço = custoFabrica + distribuidorP + impostosP
else:
    distribuidorP = (5/100) * custoFabrica
    preço = custoFabrica + distribuidorP + impostosP

print(f"R$ {preço:.2f}")
