"""https://www.acmicpc.net/problem/10162"""

import sys


def input(): return sys.stdin.readline().rstrip()


C = int(input())

A = 0
B = 0
if C % 10 != 0:
    print(-1)
else:
    A += C // 300
    C %= 300
    B += C // 60
    C = int(C % 60 / 10)
    print(A, B, C)