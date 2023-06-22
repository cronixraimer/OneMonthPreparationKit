def supperDigit(n, k):
    #...

    if len(str(n)) == 1:
        return n
    else:
        digit_sum = str(sum([int(i) for i in n])) * k
        return supperDigit(digit_sum, 1)

    #Iteration over each digit in the integer
    #n = 9876
    #k = 4

first_multiple_input = input().rstrip().split()

n = first_multiple_input[0]

k = int(first_multiple_input[1])

result = supperDigit(n, k)

print(result)
