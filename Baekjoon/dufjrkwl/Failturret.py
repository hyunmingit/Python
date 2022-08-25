"""https://www.acmicpc.net/problem/1002"""

import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())

for i in range(N):
    x = 0
    y = 0
    a, b, r, aa, bb, rr = map(int, input().split())
    dis = ((aa - a) ** 2 + (bb - a) ** 2)
    if rr - r < 0:
        rdif = r - rr
    else:
        rdif = rr - r

    if a == aa and b == bb and r == rr:
        print(-1)
        continue
    elif dis == (rr + r) ** 2 or dis == rdif ** 2:
        print(1)
    elif rdif ** 2 < dis < (rr + r) ** 2:
        print(2)
    else:
        print(0)
