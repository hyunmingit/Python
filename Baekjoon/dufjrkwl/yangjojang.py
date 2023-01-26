"""https://www.acmicpc.net/problem/11557"""

import sys

def input(): return sys.stdin.readline().rstrip()


T = int(input())

for i in range(T):
    univ = {}
    C = int(input())
    for j in range(C):
        A,B = map(input().split())
        univ[A] = int(B)
