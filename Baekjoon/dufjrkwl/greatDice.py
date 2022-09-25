"""https://www.acmicpc.net/problem/10103"""


import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())
Cs = 100
Ss = 100
for i in range(N):
    A, B = map(int, input().split())
    if A == B:
        continue
    elif A > B:
        Ss -= A
    else:
        Cs -= B

print(Cs)
print(Ss)