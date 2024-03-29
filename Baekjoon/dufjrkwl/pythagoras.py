"""https://www.acmicpc.net/problem/4153"""

import sys


def input(): return sys.stdin.readline().rstrip()


while True:
    x, y, z = map(int, input().split())
    if x == 0 and y == 0 and z == 0:
        break

    if x ** 2 + y ** 2 == z ** 2 or y ** 2 + z ** 2 == x ** 2 or z ** 2 + x ** 2 == y ** 2:
        print('right')
    else:
        print('wrong')

