"""https://www.acmicpc.net/problem/2447"""

import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())

star = "*"
cnt = 0



M = N
cnt = 0
while True:
    if M == 1:
        break
    M /= 3
    cnt += 1

enter = '\n'
space = ' '
result = ''
