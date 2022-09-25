"""https://www.acmicpc.net/problem/10817"""


import sys


def input(): return sys.stdin.readline().rstrip()


A, B, C = map(int, input().split())


if A >= B >= C or C >= B >= A:
    print(B)
elif C >= A >= B or B >= A >= C:
    print(A)
else:
    print(C)

