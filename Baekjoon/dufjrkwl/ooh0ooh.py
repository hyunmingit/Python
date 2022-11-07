"""https://www.acmicpc.net/problem/10988"""

import sys


def input(): return sys.stdin.readline().rstrip()


P = list(input())
R = []
for i in range(len(P)-1, -1, -1):
    R.append(P[i])
if P == R:
    print(1)
else:
    print(0)
