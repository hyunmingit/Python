"""https://www.acmicpc.net/problem/2108"""

N = int(input())
nums = []
for i in range(N):
    nums.append(int(input()))

nums = sorted(nums)  # 오름차순
cen = int((N - 1) / 2)  # 중앙값 인덱스
print(round(sum(nums) / N))  # 평균
print(nums[cen])  # 중앙값
if len(nums) == 1:  # 길이가 1이면 바로 출력
    print(nums[0])
elif len(nums) == len(set(nums)):  # 중복이 없으면 두 번째로 큰 수 바로 출력
    print(nums[1])
else:
    x = {}  # 숫자와 빈도수 딕셔너리
    for value in nums:  # 딕셔너리에 빈도수와 함께 저장
        try:            #key가 존재 한다면 += 1 하고 존재하지 않아 오류가 발생하면 1 부여
            x[value] += 1
        except Exception:
            x[value] = 1

    res1 = max(x, key=x.get)  # 빈도수가 큰것중 가장 작은 수
    re1 = x[res1]  # 위 숫자의 value
    del x[res1]  # 두번째로 작은수 찾기위해 가장 작은 수 제거
    res2 = max(x, key=x.get)  # 두번째로 작은 수

    if re1 == x[res2]:  # 처음 꺼낸 수와 두번째로 꺼낸 숫자 빈도수가 같으면 두번째로 작은수 출력
        print(res2)
    else:  # 처음 숫자의 빈도가 더 크므로 첫번째 숫자 출력
        print(res1)
print(nums[-1] - nums[0])  # 범위


