"""https://www.acmicpc.net/problem/1181"""

num = int(input())
words = {}
big = 0
for i in range(num):
    word = input()
    words[word] = len(word)
    if len(word) > big:
        big = len(word)

newwords = sorted(words.items())
print(newwords)
cnt = 2
for k in range(2, big+1):
    for j in newwords:
        if newwords[j] < k and newwords[j] != 0:
            print(j)
            newwords[j] = 0

