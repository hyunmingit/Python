N, M = map(int, input().split())

P = []

"""떼어낸 체스판"""
num = []
"""카운트 횟수 리스트"""
counts = []

"""한 글자씩 리스트에"""
for i in range(N):
    s = input()
    for w in range(len(s)):
        P.append(s[w])


def counting(numli):
    count = 0

    for j in range(8):
        for y in range(7):
            if numli[j][y] == numli[j][y + 1] and numli[j][y + 1] == 'B':
                numli[j][y + 1] = 'W'
                count += 1
            elif numli[j][y] == numli[j][y + 1] and numli[j][y + 1] == 'W':
                numli[j][y + 1] = 'B'
                count += 1
            """행의 마지막 다음행 처음"""
            if y == 6 and j < 7:
                if numli[j][y + 1] != numli[j + 1][0]:
                    numli[j + 1][0] = numli[j][y + 1]
                    count += 1
    """과반수 이상 바꾸면 흑과 백을 반대로 바꾸는게 카운트가 더 작음"""
    if count > 32:
        count = 64 - count
        return count
    return count


for o in range(N - 7):
    for q in range(M - 7):
        num = []
        for z in range(8):
            num.append(P[0 + q + (o + z) * M: 8 + q + (o + z) * M])
            """8 * 8 체스판 떼어 오기"""
        counts.append(counting(num))
print(min(counts))


