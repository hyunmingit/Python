"""https://www.acmicpc.net/problem/2525"""

import sys


def input() : return sys.stdin.readline().rstrip()



H, M = map( int, input().split())


N = int(input())

H += (M+N) // 60

M = (M + N) % 60


if H >= 24:
    H -= 24

print(H, M)
