"""
이름 장현민
내용 파이썬 선택 정렬 알고리즘 실습
"""

dataset = [3, 5, 1, 2, 4]
n = len(dataset)

for i in range(0, n-1):
    for j in range(i+1, n):
        if dataset[i] > dataset[j]:

            a = dataset[i]
            dataset[i] = dataset[j]
            dataset[j] = a






    print(dataset)


