"""https://www.acmicpc.net/problem/11399"""

import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())
nli = sorted(list(map(int, input().split())))
res = 0
cnt = 0
for i in nli:
    res += i * (len(nli) - cnt)
    cnt += 1

print(res)
