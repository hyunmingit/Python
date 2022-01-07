"""
파이썬 챕터2 실습
2022/01/03
장현민
"""

# 변수와 메모리 주소

var1 = "Hello python"
print(var1)
print(id(var1))

var1 = 100
print(var1)
print( id(var1) )

var2 = 150.25
print(var2)
print( id(var2) )


#예약어 확인

import  keyword #모듈 임포트
python_keyword = keyword.kwlist
print(python_keyword)

print( type(python_keyword) )
print( len(python_keyword) )

#자료형
var1 = "Hello python"
print(var1)
print( type(var1))

var1 = 100
print(var1)
print(type(var1))

var2 = 150.25
print( type(var2))

var3 = True
print( type(var3))

a = int(10.5)
b = int(20.42)
add = a + b
print('add = ', add)

a = float(10)
b = float(20)
add2 = a + b
print('add2 = ', add2)

print( int(True))
print( int(False))

st = '10'
print( int(st) ** 2 )

num1 = 100
num2 = 20

add = num1 + num2
print(add)
sub = num1 - num2
print(sub)
mul = num1 * num2
print(mul)
div = num1 / num2
print(div)
div2 = num1 % num2
print(div2)
square = num1**2
print(square)


bool_result = num1 ==num2
print((bool_result))
bool_result = num1 != num2
print(bool_result)

bool_result = num1 > num2
print(bool_result)
bool_result = num1 >= num2
print(bool_result)
bool_result = num1 < num2
print(bool_result)
bool_result = num1 <= num2
print(bool_result)

log_result = num1 >= 50 and num2 <= 10
print(log_result)

log_result = num1 >=50 or num2 <= 10
print(log_result)

log_result = num1 >= 50
print(log_result)

log_result = not(num1 >= 50)
print(log_result)


i = tot = 10
i += 1
tot += i
print(i, tot)

print('출력1', end=' , ')
print('출력2')

v1, v2 = 100, 200
v2, v1 = v1, v2
print(v1, v2)

lst = [1, 2, 3, 4, 5]
v1, *v2 = lst
print(v1, v2)

*v1, v2 = lst
print(v1, v2)

num = input("숫자입력 : ")
print('num type :', type(num))
print('num = ', num)
print('num = ', num*2)

num1 = int( input("숫자입력: "))
print('num1 = ', num1*2)

num2 = float(input("숫자입력 :"))
result = num1 + num2
print('result =', result)

