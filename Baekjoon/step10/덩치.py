N = int(input())
weight = [0 for i in range(N)]
height = [0 for j in range(N)]
rank = [1 for h in range(N)]
for k in range(N):
    weight[k], height[k] = map(int, input().split())




for l in range(N):
    for n in range(l+1, N):
        if weight[l] > weight[n] and height[l] > height[n]:
            rank[n] += 1
        elif weight[n] > weight[l] and height[n] > height[l]:
            rank[l] += 1
for i in rank:
    print(i, end=' ')

