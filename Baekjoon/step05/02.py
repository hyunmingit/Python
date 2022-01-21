
import sys
data=[]
n = 9
for i in range(n):
    data.append(list(map(int,sys.stdin.readline().split())))


print(max(data)[0])

Kk = data.index(max(data))+1
print(Kk)



