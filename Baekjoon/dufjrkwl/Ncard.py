"""https://www.acmicpc.net/problem/10815"""

import sys


def input(): return sys.stdin.readline().rstrip()


N = int(input())
cnt = 0

my_cards = list(map(int, input().split()))

my_cards = set(my_cards)

M = int(input())

new_cards = list(map(int, input().split()))

res ={}
for i in new_cards:
    res[i] = 0

new_cards = set(new_cards)

for card in new_cards:
    if card in my_cards:
        res[card] = 1

for value in res.values():
    print(value, end=' ')


