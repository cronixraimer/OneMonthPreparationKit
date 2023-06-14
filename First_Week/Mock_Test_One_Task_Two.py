#Mock Test From First Week!
def flippingMatrix(matrix):

     max_sum = 0  # Initialize the maximum sum to 0

     for i in range(n):  # Iterate over rows
            for j in range(n):  # Iterate over columns
            # Calculate the sum of four cells in the upper-left quadrant
                max_sum +=max (
                    matrix[i][j],
                    matrix[2 * n - 1 - i][j],\
                    matrix[i][2 * n - 1 - j],
                    matrix[2 * n - 1 - i][2 * n - 1 - j]
                    )

            # Update the maximum sum if necessary
            #max_sum = max(max_sum, current_sum)

     return max_sum


q = int(input().strip())
for i in range(q):
    n = int(input().strip())

    matrix = []

    for j in range(2 * n):
        matrix.append(list(map(int, input().rstrip().split())))

    result = flippingMatrix(matrix)

    print(str(result))
