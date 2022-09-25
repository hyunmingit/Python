"""https://www.acmicpc.net/problem/2530"""

import sys

def input(): return sys.stdin.readline().rstrip()


A, B, C = map(int, input().split())
s = int(input())

h = s // 3600
s %= 3600
m = s // 60
s %= 60

A += h
B += m
C += s

if C >= 60:
    B += 1
    C -= 60
if B >= 60:
    A += 1
    B -= 60
if A >= 24:
    A = A % 24

print(A, end=' ')
print(B, end=' ')
print(C)

