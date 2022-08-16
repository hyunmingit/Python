"""https://www.acmicpc.net/problem/1929"""

a, b = map(int, input().split())
if a == 1:
    a += 1
if a % 2 == 1:
    prime = list(range(a, b + 1, 2))
elif a == 2:
    prime = list(range(a + 1, b + 1, 2))
    prime.insert(0, 2)
else:
    prime = list(range(a + 1, b + 1, 2))
m = int(b ** 0.5)
for i in range(3, m + 1):
    j = 2
    while j != i:
        if i % j == 0:
            try:
                prime.remove(i)
                break
            except:
                break

        j += 1

    for k in range(i + i, b + 2, i):
        try:
            prime.remove(k)
        except:
            pass
for num in prime:
    print(num)
