
n = int(input())
wh = list(map(str, input().split()))
arr = []

for i in range(n):
    for k in range(n):
        x = i + 1
        y = k + 1
        arr.append([x, y])

loc = 0

Y = arr[loc][0]
X = arr[loc][1]
for j in wh:
    if j == 'U':
        if Y != 1:
            loc -= n
    elif j == 'D':
        if Y != n:
            loc += n
    elif j == 'L':
        if X != 1:
            loc -= 1
    elif j == 'R':
        if X !=n:
            loc += 1


print(arr[loc][0], end=" ")
print(arr[loc][1])





