"""
날짜 2022.01.06
이름 장현민
내용 파이썬 예외처리 실습 p212
"""
print('start...')
print('='*20)

#try ~except
num1, num2 = 1, 0

r1 = num1 + num2
r2 = num1 - num2
r3 = num1 * num2
r4 = 0
try:
    r4 = num1 / num2
except: #예외 할때 처리할 코드
    print('예외...')

print(r1)
print(r2)
print(r3)
print(r4)


print(end='='*7)
print(end='Phase2')
print('='*7)
#try ~except ~ finally
try:
    r4 = num1 / num2
except Exception as e:
    print('에러 : ', e)
finally:                # 에러 발생 여부와 상관 없이 무조건 실행 코드 블럭
    print('No error...')

animal = {'Tiger', 'Eagle', 'Shark'}
result = None

while True:
    try:
        print('Animal Choose')
        print('1:Tiger, 2:Eagle, 3:Shark, 0:Exit')
        answer = int(input('Num : '))
        if answer == 0:
            print('Exit...')
            break
        result = animal[answer-1]
    except Exception as e:
        print('Error : ', e)

    finally:
        if result != None:
            print(' Animal is... %s' % result)



print('='*20)
print('finish...')
