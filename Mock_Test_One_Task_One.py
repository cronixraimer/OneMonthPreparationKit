#Mock Test From First Week!
def findMedian(arr):
    sorted_arr = sorted(arr)
    middle_index = (len(sorted_arr) - 1) // 2
    median = sorted_arr[middle_index]

    return median


n = int(input().strip())
arr = list(map(int, intput().rstrip().split()))


result = findMedian(arr)

print(result)
