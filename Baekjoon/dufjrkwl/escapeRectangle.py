"""https://www.acmicpc.net/problem/1085"""

import sys
def input() : return sys.stdin.readline().rstrip()


x, y, w, h = map(int, input().split())

res = []

res.append(x)
res.append(y)
res.append(w-x)
res.append(h-y)

print(min(res))
