"""https://www.acmicpc.net/problem/5086"""

import sys


def input(): return sys.stdin.readline().rstrip()


while True:
    N, M = map(int, input().split())
    if N == 0:
        break

    if N % M == 0:
        print('multiple')
    elif M % N == 0:
        print('factor')
    else:
        print('neither')