N, M = map(int, input().split())

card = list(map(int, input().split()))
card.sort()

res = []

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            R = card[i] + card[j] + card[k]
            if R <= M:
                res.append(R)

print(max(res))





