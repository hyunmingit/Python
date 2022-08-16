N = int(input())
numli = []
for i in range(N):
    numli.append(int(input()))

for j in range(N-1):
    for k in range(N-1):
        if numli[k] > numli[k+1]:
            temp = numli[k]
            numli[k] = numli[k+1]
            numli[k+1] = temp



for num in numli:
    print(num)

