def supperDigit(n, k):
    #...
    digit = int(n)

    if digit < 10:
        return digit
    else:
        digit_sum = sum(int(i) for i in str(digit))
        return digit_sum

    #Iteration over each digit in the integer
    #n = 9876
    #k = 4

first_multiple_input = input().rstrip().split()

n = first_multiple_input[0]

k = int(first_multiple_input[1])

result = supperDigit(n, k)

print(result)
