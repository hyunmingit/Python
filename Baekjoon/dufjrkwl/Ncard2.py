"""https://www.acmicpc.net/problem/10816"""

import sys
def input(): return sys.stdin.readline().rstrip()

N = int(input())

data = {}
refs = list(map(int, input().split()))

for ref in refs:
    try:
        data[ref] += 1
    except Exception:
        data[ref] = 1

M = int(input())

mcards = list(map(int, input().split()))

for card in mcards:
    try:
        print(data[card], end=' ')
    except:
        print(0, end=' ')

