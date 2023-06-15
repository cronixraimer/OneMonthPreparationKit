def sockMerchant(n, arr):
    #...
    pairs = 0
    for i in set(arr):
        pairs += arr.count(i) // 2

    return pairs

n = int(input().strip())

arr = list(map(int, input().rstrip().split()))

result = sockMerchant(n, arr)

print(str(result))
