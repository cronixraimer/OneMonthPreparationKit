def dynamicArray(n, queries):
    #...
    ans = []
    arr = []

    for i in range(n):
        arr.append([])
    last_answer = 0

    for j in queries:
        idx = (j[1] ^ last_answer) % n
        if j[0] == 1:
            arr[idx].append(j[2])
        else:
            last_answer = arr[idx][j[2] % len(arr[idx])]
            ans.append(last_answer)

    return ans

first_mitiple_input = input().rstrip().split()

n = int(first_mitiple_input[0])

q = int(first_mitiple_input[1])

queries = []

for i in range(q):
    queries.append(list(map(int, input().rstrip().split)))

result = dynamicArray(n, queries)

print(result)
