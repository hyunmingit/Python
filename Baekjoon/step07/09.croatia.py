word = input()

num1 = word.count("c-")
num2 = word.count('c=')
num3 = word.count('dz=')
num4 = word.count('d-')
num5 = word.count('lj')
num6 = word.count('nj')
num7 = word.count('s=')
num8 = word.count('z=')


if num3 != 0:
    num7 -= num3


rs = len(word) - (num1+num2+num3*2+num4+num5+num6+num7+num8)
print(rs)
