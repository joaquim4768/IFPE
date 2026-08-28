import math

a = int(input())
b = int(input())
operacao = int(input())

match operacao:
    case 1:
        print(f"{a ** b:.1f}")
    case 2:
        print(f"{a ** 2 + b ** 2:.1f}")
    case 3:
        print(f"{math.sqrt(a) + math.sqrt(b):.1f}")
    case _:
        print("ERRO")