"""
장현민
2022.01.04
교재 복습
"""
score = int(input('점수 : '))
grade =''
if score >=85:
    grade = 'good'
elif score >= 70:
    grade ='soso'
else: grade = 'bad'

print('점수는 %d 이고, 등급은%s' %(score, grade))
