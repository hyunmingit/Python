"""https://www.acmicpc.net/problem/25305"""

N, k = map(int, input().split())
k *= -1
scores = sorted(list(map(int, input().split())))

print(scores[k])
