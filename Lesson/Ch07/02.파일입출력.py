"""
날짜 2022.01.06
이름 장현민
내용 파이썬 파일 입출력 실습 p217
"""

# 파일 읽기
f1 = open('Test.txt', mode='r', encoding='utf-8')

while True:
    #줄 별로 읽기
    line = f1.read()

    if not line:
        break

    print(line)

f1.close()


# 파일 쓰기

f2 = open('./Result.txt', mode='w', encoding='utf-8')
f2.write('안녕하세요.\n')
f2.write('반갑.\n')
f2.write('건강하세요.\n')
f2.close()

#구구단 쓰기
f3 = open('./multiple.txt', mode='w', encoding='utf-8')


for a in  range(2,10):
    f3.write('%d단\n' % a)
    print(f' {a}단')
    for b in  range(1,10):
         f3.write(f'{a} x {b} = {a * b}\n')



