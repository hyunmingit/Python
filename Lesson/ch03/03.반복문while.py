"""
날짜 : 2022/01/03
이름 : 장현민
내용 : 파이썬 반목문 실습 p701
"""

#while문
i = 1

while i <= 5 :
    print('반복 i :', i)
    i += 1




tot, k = 0, 1

while k <= 10 :

    tot += k
    k += 1

print(tot)

#홀수의 합
sum, j = 0, 1
while j <= 10:
    if j % 2 == 1:
        sum += j
    j += 1

print(sum)

#break
num = 1
while True:
    if num % 5 == 0 and num % 7 == 0:
        break

    num += 1
    print(num)

print(num)

#continue

n = 0
while n <= 10:
    n += 1

    if n % 2 == 0:
        continue
    print(n)



