n = int(input())
strN = '666'
cnt = 0
res = 665
while True:
    if '666' in str(res):
        cnt += 1
    if cnt == n:
        break

    res += 1

print(res)