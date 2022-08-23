"""https://www.acmicpc.net/problem/11478"""

import sys
def input() : return sys.stdin.readline().rstrip()


words = input()

res = []

N = len(words)

for letter in words:
    res.append(letter)

for i in range(2, N+1):
    for j in range(N-i+1):
        res.append(words[j:j+i])

res = set(res)
print(len(res))

