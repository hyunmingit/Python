"""https://www.acmicpc.net/problem/2935"""

import sys


def input(): return sys.stdin.readline().rstrip()


A = int(input())
B = str(input())
C = int(input())

if B == '*':
    print(A*C)
elif B == '+':
    print(A+C)

