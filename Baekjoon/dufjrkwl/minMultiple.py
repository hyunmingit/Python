"""https://www.acmicpc.net/problem/1934"""

import sys


def input(): return sys.stdin.readline().rstrip()



def gcd(m,n):
    if m < n:
        m, n = n, m
    if n == 0:
        return m
    if m % n == 0:
        return n
    else:
        return gcd(n, m%n)



T = int(input())

for i in range(T):
    A, B = map(int, input().split())
    print(int(A * B / gcd(A,B)))



    """
    if A > B:
        great = A
        aa = great
        less = B
    elif B > A:
        great = B
        aa = great
        less = A
    else:
        print(A)
    for j in range(great, less * great + 1, great):
        if j % less == 0:
            print(j)
            break
    """