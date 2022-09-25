"""https://www.acmicpc.net/problem/1789"""


import sys


def input(): return sys.stdin.readline().rstrip()


S = int(input())
res = 0
n = 1
m = 0

while res < S:
    res = n * (n + 1) / 2
    n += 1

if res == S:
    print(n)


