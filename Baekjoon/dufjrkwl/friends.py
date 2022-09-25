"""https://www.acmicpc.net/problem/5717"""


import sys


def input(): return sys.stdin.readline().rstrip()


while True:
    A, B = map(int, input().split())
    if A == B == 0:
        break
    else:
        print(A+B)