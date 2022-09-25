"""https://www.acmicpc.net/problem/2981"""
import sys


def input(): return sys.stdin.readline().rstrip()


T = int(input())
res = []
Ndic = {}
for j in range(T):
    Ndic[int(input())] = 0
M = min(Ndic)
for i in range(min(Ndic)):
    chk = min(Ndic) % (i+2)
    for num in Ndic:
        if num % (i+2) == chk:
            Ndic[num] = (i+2)
            chk = num % (i+2)
        else:
            break
    if Ndic[max(Ndic)] == Ndic[min(Ndic)]:
        res.append(Ndic[min(Ndic)])

res = sorted(set(res))
for nu in res:
    print(nu, end=' ')
