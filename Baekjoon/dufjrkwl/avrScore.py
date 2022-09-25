"""https://www.acmicpc.net/problem/10039"""


import sys


def input(): return sys.stdin.readline().rstrip()


res = 0
for i in range(5):
    N = int(input())
    if N < 40:
        N = 40
    res += N

print(int(res / 5))
