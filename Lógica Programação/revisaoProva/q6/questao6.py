P = int(input())
D_1 = int(input())
D_2 = int(input())

soma = D_1 + D_2
isPar = None

if soma % 2 == 0:
    isPar = True
else:
    isPar = False


if isPar == True and P == 0:
    print("0")
elif isPar == True and P == 1:
    print("1")
elif isPar == False and P == 0:
    print("1")
elif isPar == False and P == 1:
    print("0")