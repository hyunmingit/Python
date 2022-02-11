x,y = map(str, input().split())
a = int(-1)
b = -1
n=[]
m=[]
o=[]
p=[]
for i in range(len(x),0,-1):
    c=x[i-1]
    n.append(c)
for i in range(len(y),0,-1):
    c=y[i-1]
    o.append(c)
m = ''.join(n)
p = ''.join(o)


if int(m) > int(p):
    print(m)
else :
    print(p)