"""
날짜 2022.01.06
이름 장현민
내용 파이썬 내장함수 실습 p119
"""
import random
import  time
import  math

#시간 관련 함수
t1 = time.time()
print(t1)

t2 = time.ctime()
print(t2)

now = time.localtime(time.time())
year = time.strftime('%Y', now)
month = time.strftime('%m', now)
date = time.strftime('%d', now)
hour = time.strftime('%H', now)
min = time.strftime('%M', now)
sec = time.strftime('%S', now)

print('{}년 {}월 {}일 {}:{}:{}'.format(year, month, date, hour, min, sec))
#수학 관련 함수
r1 = math.ceil(1.2)
r2 = math.ceil(1.8)

print(r1)
print(r2)

r3 = math.floor(1.2)
r4 = math.floor(1.8)

print(r3)
print(r4)

r5 = round(1.2)
r6 = round(1.8)

print(r5)
print(r6)

#Random : 임의의 수를 구하는 함수
num1 = random.random()
print(num1)#0 1 사이의 랜덤 실수

num2 = num1 * 10
print(num2)

num3 = math.ceil(num2)
print(num3)

num45 = random.random() * 45
print(num45)

num9 = round(num2)
print(num9)

reult = math.ceil(random.random()*10)
print("resut ", reult)



