"""https://www.acmicpc.net/problem/3036"""

import sys


def input(): return sys.stdin.readline().rstrip()


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a



N = int(input())

rli = list(map(int, input().split()))

R = rli[0]
fli = [1]

for j in range(1, N):
    fli.append(gcd(R, rli[j]))
for i in range(1,N):
    print(str(int(R / fli[i])) + '/' + str(int(rli[i] / fli[i])))




