"""https://www.acmicpc.net/problem/1427"""
N = list(map(int, input().strip()))
N = sorted(N)
k = -1
for i in range(len(N)):

    print(N[k], end='')
    k -= 1


