R = int(input())
M = int(input())
L = int(input())

#Printa primeira linha (recorde mundial ou não)
if R < M:
    print("RM")
else:
    print("*")

#Printa segunda linha (recorde olímpico ou não)
if R < L:
    print("RO")
else:
    print("*")