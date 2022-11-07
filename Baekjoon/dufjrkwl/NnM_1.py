"""https://www.acmicpc.net/problem/15649"""

import sys


def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())


if M == 1:
    for i in range(M):
        print(i+1)
else:
