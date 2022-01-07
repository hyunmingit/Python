dataset = [3, 5, 1, 2, 4]
print(dataset)
print(len(dataset))

n = len(dataset)

for i in range(0, n-1):
    for j in range(i+1, n):
        if dataset[i] > dataset[j]:
            dataset[j] = dataset[i]


    print(dataset)


