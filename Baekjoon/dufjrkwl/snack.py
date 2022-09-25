"""https://www.acmicpc.net/problem/10156"""


import sys


def input(): return sys.stdin.readline().rstrip()


N, M, K = map(int, input().split())

res = N * M - K
if res < 0:
    print(0)
else:
    print(res)