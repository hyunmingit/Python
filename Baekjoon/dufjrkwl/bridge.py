"""https://www.acmicpc.net/problem/1010"""

import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())

for k in range(N):

    A, B = map(int, input().split())
    res = 1
    if A == B:
        print(1)
    else:
        for i in range(1, B+1):
            res *= i
        for j in range(1, A+1):
            res /= j
        for k in range(1, B-A+1):
            res /= k

        print(int(res))


