"""
날짜 2022.02.18
이름 장현민
내용 선택정렬 실습
"""


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):

    for j in range(i+1, len(arr)):

        if arr[i] > arr[j]:
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp
            print(arr)


print(arr)