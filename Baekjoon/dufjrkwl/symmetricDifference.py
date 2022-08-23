"""https://www.acmicpc.net/problem/1269"""
import sys
def input() : return sys.stdin.readline().rstrip()

N, M = map(int, input().split())

nnn = list(map(int, input().split()))
mmm = list(map(int, input().split()))

num1 = len(nnn)
num2 =len(mmm)
num3 = len(set(nnn + mmm))
dif = num1 + num2 - num3
print(num3 - dif)