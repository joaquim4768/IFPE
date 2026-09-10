a = int(input())
b = int(input())
c = int(input())

if a == 90 or b == 90 or c == 90:
    print("Retângulo")
elif a > 90 or b > 90 or c > 90:
    print("Obtusângulo")
elif a < 90 and b < 90 and c < 90:
    print("Acutângulo")