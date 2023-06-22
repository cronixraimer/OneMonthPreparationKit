def supperDigit(n, k):
    #...

    if len(str(n)) == 1: #check is length of my string one digit if yes return supperDigit
        return n
    else:
        digit_sum = str(sum([int(i) for i in n])) * k
        #str (sum(int(converting my string into integer then telling give me the sum of my string in length )))
        #then multipling it and getting all loop getting back same subsequence which is sum so until will not reach on digit
        
        return supperDigit(digit_sum, 1)

    #Iteration over each digit in the integer
    #n = 9876
    #k = 4

first_multiple_input = input().rstrip().split()

n = first_multiple_input[0]

k = int(first_multiple_input[1])

result = supperDigit(n, k)

print(result)
