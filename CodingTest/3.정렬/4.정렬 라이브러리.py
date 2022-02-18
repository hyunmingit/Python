"""
날짜 2022.02.18
이름 장현민
내용 삽입정렬 실습
"""


arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


#sorted
sorted_arr = sorted(arr)
print('sorted array : ',  sorted_arr)

sorted_arr2 = sorted(arr, reverse=True)

print('sorted array2 : ',  sorted_arr2)


#sort
arr.sort()
print('sorted array3 : ',  arr)

arr.sort(reverse=True)

print('sorted array4 : ',  arr)





#key 매개변수를 활용한 정렬

dataset = [['바나나', 2], ['사과', 5], ['당근', 3]]

def setting(data):
    return data[1]
rs1 = sorted(dataset, key=setting)
print(rs1)



