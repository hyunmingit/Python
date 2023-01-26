"""https://www.acmicpc.net/problem/1789"""

import sys


def input(): return sys.stdin.readline().rstrip()


S = int(input())

R = 19


N = 0
while True:
    N += 1
    if int(N * (N+1) / 2) + N >= S:
        break


if S == 1:
    print(1)
else:
    print(N)

cnt = 0



