"""https://www.acmicpc.net/problem/5063"""

import sys


def input(): return sys.stdin.readline().rstrip()


T = int(input())

for i in range(T):
    A, B, C = map(int, input().split())
    if B == A + C:
        print('does not matter')
    elif B > A + C:
        print('advertise')
    elif B < A + C:
        print('do not advertise')