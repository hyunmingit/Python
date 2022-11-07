"""https://www.acmicpc.net/problem/10886"""

import sys
import math


def input(): return sys.stdin.readline().rstrip()


T = int(input())
vote = 0
for i in range(T):
    A = int(input())
    if A == 1:
        vote += 1

if vote >= math.ceil(T/2):
    print('Junhee is cute!')
else:
    print('Junhee is not cute!')
