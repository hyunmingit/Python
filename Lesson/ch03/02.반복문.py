"""
날짜 : 2022/01/03
이름 : 장현민
내용 : 파이썬 반목문 실습 p701
"""


#for

for i in range(5):
    print('반복 i : ', i)

for j in  range(10, 20):
    print('반복 j : ', j)

for k in range(10, 0, -1):
    print('반복 k : ', k)

#1부터 10까지 합
tot = 0
for l in range(11):
    tot += l
    print('합 : ', tot)

#짝수의 합
sum = 0
for k in  range(11):
    if k%2 ==0:
        sum += k
        print('10까지 짝수의 합', sum)

#중첩 for
for a in  range(3):
    print('a :', a)
    for b in range(4):
        print('b :', b)
        for c in range(5):
            print('c :', c)

#구구단
for a in  range(2,10):
    print(f' {a}단')
    for b in  range(1,10):
         print(f'{a} x {b} = {a * b}')
    print()


#삼각별
for s in range(1, 11):
    for end in  range(11-s):
        print('☆', end='')

    print()


for i in  range(10, 0, -1):
    print('★' * i)

