soma = 0

while True:
    num = int(input())

    if num == 0:
        break

    if num % 5 == 0:
        soma += num

print(soma)