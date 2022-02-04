"""
각 행에서 뽑은 숫자중 가장 큰 숫자 찾기

"""

n, m = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]

result = []

for i in range(n):
    result.append(min(arr[i]))

print(max(result))

