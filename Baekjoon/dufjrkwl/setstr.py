"""https://www.acmicpc.net/problem/14425"""

import sys


def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

str1 = []
for i in range(N):
    str1.append(input())


str1 = set(str1)
res = 0

for k in range(M):
    if input() in str1:
        res += 1


print(res)
