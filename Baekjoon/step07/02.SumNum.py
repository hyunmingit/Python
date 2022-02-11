N = int(input())
K = int(input())
T=0
for i in range(N):

    T += K // 10**i % 10

print(T)