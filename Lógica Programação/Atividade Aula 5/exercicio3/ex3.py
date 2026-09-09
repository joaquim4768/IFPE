codigo = int(input())
kg = int(input())
preço = 0
valor = 0

match codigo:
    case 1:
        #maçã
        if kg > 5:
            valor = 5.8
        else:
            valor = 7
    case 2:
        #pera
        if kg > 5:
            valor = 8.5
        else:
            valor = 11.8
    case 3:
        #laranja
        if kg > 5:
            valor = 1.7
        else:
            valor = 2.25
    case 4:
        #banana
        if kg > 5:
            valor = 4
        else:
            valor = 5.5
    case 5:
        #tomate
        if kg > 5:
            valor = 5.5
        else:
            valor = 6.9
    case 6:
        #cebola
        if kg > 5:
            valor = 2.5
        else:
            valor = 4.5

preço = valor * kg

print(f"R$ {preço:.2f}")