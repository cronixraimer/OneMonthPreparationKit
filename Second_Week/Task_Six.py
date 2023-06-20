def maxMin(k, arr):
    #...
    sorted_arr = sorted(arr)

    min_diff = float('inf')
    for i in range(len(arr) - k + 1):
        subsequence = sorted_arr[i:i + k]  
        diff = subsequence[-1] - subsequence[0]
        min_diff = min(min_diff, diff)


    return min_diff





n = int(input().strip())

k = int(input().strip())

arr = []

for i in range(n):
    arr_item = int(input().strip())
    arr.append(arr_item)
result = maxMin(k, arr)

print(str(result))
