A, B = map(int, input().split())





a = list(map(int, input().split()))


for i in range(A):
    if a[i] < B:
        print(a[i], end=' ')


