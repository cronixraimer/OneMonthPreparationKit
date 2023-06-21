def balancedSums(arr):
    #...
    rightSum = 0
    leftSum = sum(arr)

    for i in arr:
        leftSum = leftSum - i
        
        if rightSum == leftSum:
            return "YES"

        rightSum = rightSum + i

    return "NO"


T = int(input().strip())

for i in range(T):
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = balancedSums(arr)

    print(result)
