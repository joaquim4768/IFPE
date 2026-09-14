saida = ""

while True:
    m, n = map(int, input().split())

    if m >= n:
        break

    soma = 0
    for i in range(m, n + 1):
        soma += i

    saida += f"{soma} "

print(saida)