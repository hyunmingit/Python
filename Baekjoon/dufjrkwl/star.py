import sys


def input() : return sys.stdin.readline().rstrip()


N = int(input())

str1 = ' '
str2 = '*'

for i in range(1, N+1):

    print(str1 * (N - i), end = '')
    print(str2 * ((2 * i) -1))
