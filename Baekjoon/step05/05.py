n = int(input())
score_list=list(map(int,input().split()))
M = max(score_list)
for i in range(n):
   score_list[i] = score_list[i] / M * 100

Rs = sum(score_list) / n
print(Rs)
