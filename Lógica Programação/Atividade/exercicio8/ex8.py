n1 = float(input())
n2 = float(input())

media = (n1 + n2) / 2

if media >= 0 and media < 3:
    print(f"{media:.1f} - Reprovado")
elif media >= 3 and media < 7:
    print(f"{media:.1f} - Exame")
elif media >= 7 and media <= 10:
    print(f"{media:.1f} - Aprovado")
else:
    print("Digite um valor válido")