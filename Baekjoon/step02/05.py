A, B = map(int, input().split())


if B >= 45:
    B -= 45
    print(A, end=' ')
    print(B)

elif A == 0 and B < 45:

    A = 23
    B = 15 + B
    print(A, end=' ')
    print(B)
elif A==0 and B >=45:
    A = 23
    print(A, end=' ')
    print(B)

else:
    A -= 1
    B = 15 + B
    print(A, end=' ')
    print(B)
