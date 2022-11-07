"""https://www.acmicpc.net/problem/7567"""

import sys


def input(): return sys.stdin.readline().rstrip()


dishes = list(input())
temp = dishes[0]
res = 10
for i in range(1, len(dishes)):
    if dishes[i] == temp:
        res += 5
    else:
        res += 10
    temp = dishes[i]
print(res)
