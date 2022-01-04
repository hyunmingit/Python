"""
날짜 : 2022/01/04
이름 : 장현민
내용 : 파이썬 for 연습문제 -정답
"""

sum = 0

for i in range (1, 11):
    for j in range(1,1+i):
        sum += j
        print('%d' %j, end='+')
    print()

print('총 합 :', sum)
