"""https://www.acmicpc.net/problem/15649"""

import sys


def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

numli = list(range(1, N+1))

tli = []
for i in range(M):
    tli.append(10**M)

res = []

for j in range(1,N+1):
    lili = []
    for k in range(1,M+1):

        lili.append(k)
    res.append(lili)

print(res)




