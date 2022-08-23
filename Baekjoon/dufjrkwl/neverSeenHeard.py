"""https://www.acmicpc.net/problem/1764"""

import sys
def input() : return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

NSH = {}
res = []
for i in range(N):
    NSH[input()] = 0

for j in range(M):
    ip = input()
    try:
        NSH[ip] #오류 생성
        res.append(ip)
    except:
        pass

print(len(res))
res = sorted(set(res))
for name in res:
    print(name)


