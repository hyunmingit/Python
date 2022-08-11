N = int(input())

M = 1

while True:
    if M == N:
        break
    its = str(M)
    num = M
    for i in range(len(its)):
        num += int(its[i])
    if num == N:
        break
    else:
        M += 1

if M == N:
    print(0)
else:
    print(M)

