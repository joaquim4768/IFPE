inteiro = int(input())
primo = True

for i in range(2, inteiro):
    if inteiro % i == 0:
        primo = False
        break

if primo == True:
    print("Sim")
else:
    print("Não")