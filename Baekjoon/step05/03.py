import math


a = int(input())
b = int(input())
c = int(input())

D = a * b * c

C0 = 0
C1 = 0
C2 = 0
C3 = 0
C4 = 0
C5 = 0
C6 = 0
C7 = 0
C8 = 0
C9 = 0

for i in range(9, 0, -1):
    N = D / (10**i)
    if N >= 1:
        K = i + 1

        break

    else:

        continue



for j in range(K):
    O = (D // (10**j)) % 10

    if O == 1:
        C1 += 1

    elif O == 0:
        C0 += 1

    elif O == 2:
        C2 += 1

    elif O == 3:
        C3 += 1

    elif O == 4:
        C4 += 1

    elif O == 5:
        C5 += 1

    elif O == 6:
        C6 += 1

    elif O == 7:
        C7 += 1

    elif O == 8:
        C8 += 1

    elif O == 9:
        C9 += 1


print(C0)
print(C1)
print(C2)
print(C3)
print(C4)
print(C5)
print(C6)
print(C7)
print(C8)
print(C9)