"""
날짜 2022.01.06
이름 장현민
내용 파이썬 리스트 함수 실습 p88
"""
import math

datset =[1, 4, 3]
print(datset)

#데이터 추가
datset.append(2)
datset.append(5)
print(datset)
#데이터 정렬
datset.sort()
print(datset)

datset.sort(reverse=True)
print(datset)
#뒤집기

datset.reverse()
print(datset)

#데이터 삽입
datset.insert(2, 6) #2 뒤에 6 삽입
print(datset)

datset.insert(1, 7) #1 뒤에 7 삽입
print(datset)

#데이터 삭제
datset.remove(6) #데이터값으로 삭제
print(datset)

datset.pop(1) #인덱스로 삭제
print(datset)

#map 함수 : 모든 원소를 함수로 처리해주는 함수
def plus10(x):
    return x+10

list1 = [1, 2, 3, 4, 5]
r1 = map(plus10, list1)
r1 = list(r1)
print(r1)


list2 = [0.1, 1.2, 2.6, 3.4, 4.9]
r2 = list(map(math.ceil, list2))
print(r2)

list3 = ['10', '20', '30', '40', '50']
r3 = list(map(int, list3))
print(r3)


