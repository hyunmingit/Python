"""
날짜 2022.02.04
이름 장현민
내용 코딩테스트 그리디 알고리즘 실습
"""

N, K =map(int, input().split())

result = 0

while True:
    if N == 1:
        break
    elif N % K == 0:
        N /= K
        result += 1
    else:
        N -= 1
        result += 1


print(result)
