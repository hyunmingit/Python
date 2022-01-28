
import sys
C = int(input())  # 케이스 갯수

for i in range(C):
    data = list(map(int, sys.stdin.readline().split()))
    N = data[0]  # i번째 케이스 점수 갯수
    A = 0   # 평균값 A
    for j in range(1, N+1):  # A를 구하기 위해 점수 합계
        A += data[j]
    A /= N  # 평균값 도출
    count = 0  # 평균 점수 보다 높은 점수를 받은 학생 수
    for k in range(1, N+1):  # count 세기

        if data[k] > A:
            count += 1
    RES = count / N * 100  # 소수점 3번째 자리 에서 반올림
    RES2 = format(RES, ".3f")

    print(f'{RES2}%')
