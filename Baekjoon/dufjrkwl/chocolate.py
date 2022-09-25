"""https://www.acmicpc.net/problem/2163"""

import sys


def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())


if N == M == 1:
    print(0)
elif N == 1 or M == 1:
    print(N * M - 1)
else:
    print((M-1) + (N-1) * M)
