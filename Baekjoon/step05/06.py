N = int(input())
graph = [input() for _ in range(N)]

for i in range(N):
    score =0
    P = 1
    for k in range(0, len(graph[i])):
        if k >= 1 and graph[i][k] == 'O' and graph[i][k] == graph[i][k-1]:
            P += 1
            score += P
        elif graph[i][k] == 'O':
            score += P

        else:
            P = 1
            continue

    print(score)

