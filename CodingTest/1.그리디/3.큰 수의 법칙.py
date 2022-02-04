"""
n개의 숫자로 m번 더해서 가장 큰 수 동일 수 는 최대 k번까지 연속가능
"""

n, m, k = map(int, input().split())
data = list(map(int, input().split()))
RS = 0
O = max(data)
data.remove(max(data))
P = max(data)
count = 0
samecount = 0
for y in range(m):
    if samecount == k:
        RS += P
        samecount = 0
    else:
        RS += O
        samecount += 1
print(RS)

