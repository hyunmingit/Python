"""https://www.acmicpc.net/problem/11047"""

import sys
def input(): return sys.stdin.readline().rstrip()


cnt = 0

ind = -1

now = 0

coins = []

N, K = map(int, input().split())

for i in range(N):
    coins.append(int(input()))

while True:
    if now == K:
        print(cnt)
        break
    if coins[ind] <= K:

        cnt += K // coins[ind]
        K = K % coins[ind]
        ind -= 1
    elif coins[ind] + now > K:
        ind -= 1
