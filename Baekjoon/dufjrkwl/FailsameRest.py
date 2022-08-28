"""https://www.acmicpc.net/problem/2981"""

import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())

"""
Nli = []

for i in range(N):
    Nli.append(int(input()))

Nli = sorted(Nli)
M = 2
chk = 1
while M < Nli[0]:
    chk = Nli[0] % M
    for k in range(1, len(Nli)):
        if Nli[k] % M == Nli[k-1] % M:
            if k == len(Nli)-1:
                print(M)
            pass
        else:
            break
    M += 1
"""

Ndic = {}

for i in range(N):
    Ndic[int(input())] = 0

M = min(Ndic)
N = 2












