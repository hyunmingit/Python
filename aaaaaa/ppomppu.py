
#a는 6개월 요금제 b는 사용 요금제
def total(a, b):
    return int(a * 1000 * 6 + b * 1000 * 18)


"""
dic = {sk1 : 99, sk2 : 59, kt1 : 99, kt2 : 69, lg1 : 95, lg2 : 61}
telecom = input('sk, kt, lg')
plan = dic[telecom + '1']
usual = dic[telecom + '2']
"""


swt = int(input('공시는 0 선약은 1을 입력'))
dev = int(input('기기값 입력'))
plan = 99
usual = 59

G = total(plan, usual)
if swt == 1:
    G = int(G * 0.75 * 0.9)
elif swt == 0:
    G = int(G * 0.9)

print('현재 2년 요금 : ', int(59000 * 18 * 0.9))
print('2년 통신 요금 총합 : ', G)
G += dev * 10000
if dev != 0:
    print('기기값 포함 : ', G)


