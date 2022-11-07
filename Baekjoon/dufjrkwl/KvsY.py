"""https://www.acmicpc.net/problem/10214"""

import sys


def input(): return sys.stdin.readline().rstrip()


T = int(input())

for i in range(T):
    A = 0
    B = 0
    for j in range(9):
        c1, c2 = map(int, input().split())
        A += c1
        B += c2
    if A > B:
        print('Yonsei')
    elif A == B:
        print('Draw')
    else:
        print('Korea')