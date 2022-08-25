"""https://www.acmicpc.net/problem/1037"""

import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())

factors = list(map(int, input().split()))

if N == 1:
    print(factors[0] ** 2)


else:
    print(max(factors) * min(factors))
