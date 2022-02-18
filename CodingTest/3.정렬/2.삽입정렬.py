"""
날짜 2022.02.18
이름 장현민
내용 삽입정렬 실습
"""

import time
start_time = float( time.time())

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


for i in range(1, len(arr)):

    for j in range(i, 0, -1):
        if arr[j] < arr[j-1]:
            tmp = arr[j-1]
            arr[j-1] = arr[j]
            arr[j] = tmp

        else:

            break




print(arr)

end_time = float(time.time())
ttime = end_time - start_time
print(ttime)