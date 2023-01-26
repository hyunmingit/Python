"""https://www.acmicpc.net/problem/15649"""

import sys


def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

numli = list(range(1, N+1))

res = []

tli = []

for i in range(M):
    for num in numli:
        tli.append(num * 10 ** i)

print(tli)
chk = list(range(M))
for j in range(N):
    mn = 0
    mn += tli[j]






