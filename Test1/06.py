"""
날짜 : 2022/01/04
이름 : 장현민
내용 : 파이썬 for 연습문제 -정답
"""


for i in range(1,7):
    for j in range (1,7):
        tot = i + j
        if tot ==6:
            print('첫번째 수 : %d, 두번째 수 : %d ' % (i, j))