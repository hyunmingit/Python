

A = int(input())
count = 1
C = A // 10
D = A % 10
Num = D * 10 + (C + D) % 10
while True:


    if A != Num:
         Num = (Num % 10) * 10 + (Num // 10 + Num % 10) % 10
         count += 1


    elif A == Num:
        print(count)
        break







