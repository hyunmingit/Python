"""https://www.acmicpc.net/problem/1676"""
import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())

num = 1
res = 0

for i in range(1,N+1):
    if i % 125 == 0:
        res += 3
    elif i % 25 == 0:
        res += 2
    elif i % 5 == 0:
        res += 1

print(res)