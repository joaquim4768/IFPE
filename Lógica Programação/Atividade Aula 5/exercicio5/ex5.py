valor = float(input())
codigo = int(input())
parcela = codigo
descontoPar = 0

match codigo:

    case 1:
        descontoPar = 30/100
    case 2:
        descontoPar = 20/100
    case 3:
        descontoPar = 10/100
    case 4:
        descontoPar = 0
    case _:
        print("ERRO")
        exit()

valorParcela = (valor / parcela) * (1 - descontoPar) 
print(f"{parcela}x de R$ {valorParcela:.2f}")