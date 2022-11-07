"""https://www.acmicpc.net/problem/2004"""

import sys


def input(): return sys.stdin.readline().rstrip()


def div(a, b):
    exam = 1
    ff = 0
    while b ** exam <= N:
        ff += a // (b ** exam)
        exam += 1

    return ff


N, M = map(int, input().split())

cntF = div(N, 5) - div(M, 5) - div(N-M, 5)
cntT = div(N, 2) - div(M, 2) - div(N-M, 2)

if cntT > cntF:
    print(cntF)
else:
    print(cntT)


