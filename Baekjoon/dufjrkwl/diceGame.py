"""https://www.acmicpc.net/problem/2476"""


import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())
score = []
dice = []
for i in range(N):
    res = 0
    A, B, C = map(int, input().split())
    if A == B == C:
        res = 10000 + A * 1000
    elif A == B or B == C:
        res = 1000 + B * 100
    elif C == A:
        res = 1000 + C * 100
    else:
        if A > B:
            if A > C:
                res = A * 100
            else:
                res = C * 100
        else:
            if B > C:
                res = B * 100
            else:
                res = C * 100
    score.append(res)

print(max(score))

