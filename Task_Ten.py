def twoArrays(k, A, B):
    #From explanation of task it was very hard unless I did not get the main challange 
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i] + B[i] < k:
            return 'NO'
    return 'YES'

q = int(input().strip())
for i in range(q):
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    B = list(map(int, input().rstrip().split()))

    result = twoArrays(k, A, B)

    print(result)
