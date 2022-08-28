"""https://www.acmicpc.net/problem/2609"""

import sys


def input(): return sys.stdin.readline().rstrip()


N, M = map(int, input().split())

nn = N
mm = M
#시간 초과
"""
if N > M:
    great = N
    less = M
else:
    great = M
    less = N


for i in range(less, 0, -1):
    if great % i == 0 and less % i == 0:
        print(i)
        break


for j in range(great, great * less + 1):
    if j % great == 0 and j % less == 0:
        print(j)
        break

"""



ND = {}
MD = {}
num = 2

while True:
    if N == 1:
        break
    elif N % num == 0:
        N /= num
        try:
            ND[num] += 1
        except:
            ND[num] = 1
    else:
        num += 1

num = 2
while True:
    if M == 1:
        break
    elif M % num == 0:
        M /= num
        try:
            MD[num] += 1
        except:
            MD[num] = 1
    else:
        num += 1


factors = {}
factor = 1
for i in ND:
    try:
        if ND[i] > MD[i]:
            factor = factor * (i ** MD[i])
        else:
            factor = factor * (i ** ND[i])

    except:
        continue


print(factor)



num2 = 2
multi = nn * mm / factor
print(int(multi))
