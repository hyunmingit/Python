"""
장현민
2022.01.04
교재 복습
"""
#무조건 1이 되는 조건문
num = int(input('숫자입력 : '))
while num != 1:
    if num % 2 ==0:
        num /= 2
        print(num)

    elif num == 1:
        break
    else:
        num *= 3
        num += 1
        print(num)
        continue



print(num)
