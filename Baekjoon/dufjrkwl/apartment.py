"""https://www.acmicpc.net/problem/2775"""

import sys


def input(): return sys.stdin.readline().rstrip()


T = int(input())


def hap(x):
    pop = x * (x + 1) / 2
    return pop


upper = {}
lower = {}
for i in range(T):
    k = int(input())
    n = int(input())
    if n == 1:
        print(1)
    elif k == 1:
        print(int(hap(n)))
    else:
        lower[1] = 1
        upper[1] = 1
        for p in range(n):
            lower[p+1] = p+1
        for f in range(k):
            for l in range(2,n+1):
                upper[l] = upper[l-1] + lower[l]
            lower = upper
        print(upper[n])



