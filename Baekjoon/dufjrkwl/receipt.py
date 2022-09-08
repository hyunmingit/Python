"""https://www.acmicpc.net/problem/25304"""



import sys


def input(): return sys.stdin.readline().rstrip()


K = int(input())

N = int(input())

price = 0

for i in range(N):
    g, p = map(int, input().split())
    price += g * p

if price == K:
    print('Yes')
else:
    print('No')
