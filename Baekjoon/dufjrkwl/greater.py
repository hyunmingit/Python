"""https://www.acmicpc.net/problem/4101"""


import sys

def input(): return sys.stdin.readline().rstrip()


while True:
    N, M = map(int, input().split())
    if N == M == 0:
        break
    else:
        if N > M:
            print('Yes')
        else:
            print('No')