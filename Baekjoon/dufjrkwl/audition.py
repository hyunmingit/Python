"""https://www.acmicpc.net/problem/10102"""


import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())

vote = list(input())
a = 0
b = 0
for i in range(N):
    if vote[i] == 'A':
        a += 1
    else:
        b += 1

if a > b:
    print('A')
elif b > a:
    print('B')
else:
    print('Tie')
