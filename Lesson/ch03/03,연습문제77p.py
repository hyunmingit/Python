"""
날짜 : 2022/01/03
이름 : 장현민
내용 : 파이썬 반목문 실습 p701
"""



import random
print('숫자 맞추기 게임!')
com = random.randint(1, 100)
num0 = 0
while True :
    num = int(input('숫자 : '))
    if num == com:
          print(f'{num0 + 1}번 만에성공')
          break
    if num > com:
          print('다운')
          num0 += 1
          continue

    if num < com:
          print('업')
          num0 += 1
          continue

