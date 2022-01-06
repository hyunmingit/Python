


t = (10, )
print(t)

t2 = (1, 2, 3, 4, 5, 3)
print(t2)

print( t2[0], t2[1:4], t2[-1])

#튜플은 수정이 불가하다
##t2.append(t)
##print(t2) 에러

for i in t2 :
    print(i,end=' ')


print()
if 6 in t2:
    print('66666')
else:print('00000')

