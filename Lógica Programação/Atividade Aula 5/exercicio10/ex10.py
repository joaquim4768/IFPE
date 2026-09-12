somaNotas = 0

i = 0

while True:
    nota = float(input())

    if nota < 0:
        break

    somaNotas += nota
    i += 1

media = somaNotas / i
print(media)
