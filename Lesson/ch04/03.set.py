"""
날짜 2022.01.04
이름 장현민
내용 파이썬 자료구조 set 실습하기 p96
"""

#Set(집합) 순서가 없어서 index번호 없음 순서가 없으므로 중복도 없음

set1 = {1, 2, 3, 4, 5, 3, 2} # 1, 2, 3, 4, 5로 저장됨
print('set1 type :', type(set1))
print('set1 :', set1)

set2 = set('Hello World')
print('set2 type :', type(set2))
print('set2 :', set2)
#리스트로 변환해서 출력

list1 = list(set1)
print('list1 :', list1)

list2 = list(set2)
print('list2 :', list2)