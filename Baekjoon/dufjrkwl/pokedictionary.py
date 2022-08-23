"""https://www.acmicpc.net/problem/1620"""

import sys

def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())
poks = {}
for i in range(1,N+1):
    poks[input()] = i
cnt = 1
stringpoks = {}
for pok in poks:
    stringpoks[cnt] = pok
    cnt += 1
for j in range(M):
    ip = input()
    try:
        print(poks[ip])
    except:
        print(stringpoks[int(ip)])