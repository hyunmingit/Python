"""
날짜 2022.01.04
이름 장현민
내용 파이썬 자료구조 tuple 실습하기  p92
list는 동적 tuple은 정적
"""

#튜플
dataset = (1, 2, 3, 4, 5)
print('dataset type ;', type(dataset))
print('dataset :', dataset)
print('dataset[0] :', dataset[0])
print('dataset[1] :', dataset[1])
print('dataset[2] :', dataset[2])
print('dataset[3] :', dataset[3])

#튜플 수정, 추가 ,삭제 불가능

"""
dataset[1] = 7
dataset[1] = []
dataset[1:3] = []
print('dataset :', dataset) <<<오류남
"""