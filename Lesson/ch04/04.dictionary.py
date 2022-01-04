"""
날짜 : 2022/01/04
이름 : 장현민
내용 : 파이썬 자료구조 Dictionary 실습 p98

"""

#딕셔너리
dic1 = {'A':'Apple', 'B':'Banana', 'C':'cherry'}

print('dic1 type:', type(dic1))
print('dic1 :', dic1)
print("dic1['A'] :", dic1['A'])
print("dic1['B'] :", dic1['B'])
print("dic1['C'] :", dic1['C'])

bic2 = {1:'서울',
        2:'대전',
        3:'대구',
        4:'부산',
        5:'광주'}
print('bic2 :', bic2)
print("bic2[1] :", bic2[1])
print("bic2[3] :", bic2[3])
print("bic2[5] :", bic2[5])

dic3 = {
    101: [1, 2, 3, 4, 5],
    201: (6, 7, 8, 9, 10),
    103: {'한국', '미국', '일본'},
    104: {'p1':['김유신','유신'], 'p2':'김춘추', 'p3':'장보고'}
       }
print(dic3)
print('aa:', dic3[101][4])
print('bb:', dic3[201][1])
print('cc:', list(dic3[103])[0])
print('dd:', dic3[104]['p1'[0]])

