arr = [input()]
lst = list(arr)

for i in range(len(arr)):
    k = int(ord(arr[i]))
    if k < 97:
        arr[i] = chr(k+32)


print(arr)

