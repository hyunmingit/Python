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
                print(M, end=' ')
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

while N < min(Ndic):
    chk = min(Ndic) % N
    for num in Ndic:
        if num % N == chk:
            Ndic[num] = N
        else:
            break
        chk = num % N

    if Ndic[max(Ndic)] == Ndic[min(Ndic)]:
        print(Ndic[max(Ndic)], end=' ')
    N += 1



















