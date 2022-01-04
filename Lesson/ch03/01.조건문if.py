"""
날짜 : 2022/01/03
이름 : 장현민
내용 : 파이썬 조건문 실습 p68
"""

print('Hello World')

#if
num1, num2 = 1, 2

if num1 > 0:
    print('num1은 0보다 크다.')

if num1 > num2:
        print('num1은 num2보다 크다.')

if num1 > 0:
    if num2 > 1:
        print('num1은 0보다 크고, num2는 1보다 크다.')

if num1 > 0 and num2 > 1:
                print('num1은 0보다 크고 그리고 num2는 1보다 크다.')
#if ~ else
num3, num4 = 3, 4

if num3 > num4:
    print('num3은 num4보다 크다.')
    pass
else:
 print('num3은 num4보다 작다.')
 pass

#if ~ elif ~ else

if num1 > num2:
    print('num1은 num2보다 크다.')
elif num2 > num3:
    print('num2은 num2보다 크다.')
elif num3 > num4:
    print('num3은 num4보다 크다.')
else:
    print('num4가 가장 크다.')