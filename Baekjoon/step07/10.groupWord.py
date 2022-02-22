N = int(input())
cot = 0
for i in range(N):
    word = list(input().split())
    print(word)
    if len(word) <= 2:
        cot += 1
    else:
        for j in range(len(word)):
            if word[j] == word[j+1]:
                del word[j]

        if len(word) ==len(set(word)):
            cot += 1

print(cot)