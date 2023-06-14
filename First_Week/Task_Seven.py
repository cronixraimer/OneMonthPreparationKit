
def diagonalDifference(arr):
    diagonal_sum = []
    n = len(arr) # Number of rows or columns in the matrix

    #Sum of elements along the main diaginal
    main_diagonal_sum = sum(arr[i][i] for i in range(n))
    

    #Sum of elements along the secondary diagonal
    secondary_diagonal_sum = sum(arr[i][n - i - 1] for i in range(n))


    diagonal_sum = abs(main_diagonal_sum - secondary_diagonal_sum)
    return diagonal_sum

n = int(input())
arr = []

for i in range(n):
    arr.append(list(map(int, input().strip().split())))

result = diagonalDifference(arr)
print(result)
