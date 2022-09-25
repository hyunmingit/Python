"""https://www.acmicpc.net/problem/2914"""

import sys


def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

if N == 1:
    print(M)
else:
    print(N * M - N + 1)