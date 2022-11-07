"""
https://www.acmicpc.net/problem/1651
"""
"""
solution : 
여러개로 쪼개서 다른 원소들로 만들수 있는지 확인

"""


N = int(input())
codes = []
cnt = 0
res = []

for i in range(N):
    codes.append(input())
print(codes)
for code in codes:
    if len(code) < 3:
        continue
    else:
        cnt = 0
        for k in codes:
            """여기가 핵심"""
        if cnt >= 3:
            res.append(len(code))

if len(res) == 0:
    print(-1)
else:
    print(min(res))


