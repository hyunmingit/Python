"""
날짜 2022.02.11
이름 장현민

"""

n = int(input())

count = 0

for i in range(n+1):
    for j in range(60):
        for k in range(60):

            if i % 10 == 3 or j % 10 == 3 or k % 10 == 3:
                count += 1
            elif 30 <= j <= 39 or 30 <= k <= 39:
                count += 1



print(count)
