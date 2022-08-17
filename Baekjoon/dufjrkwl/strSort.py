"""https://www.acmicpc.net/problem/1181"""

import sys
def input(): return sys.stdin.readline().rstrip()


N = int(input())

words = []
bigg = 0
for i in range(N):
    hi = input()
    words.append(hi)
    if len(hi) > bigg:
        bigg = len(hi)
words = sorted(words)



Nwords = []

for k in range(bigg+1):
    for word in words:
        if len(word) == k:
            if word not in Nwords:
                Nwords.append(word)

for j in Nwords:
    print(j)

