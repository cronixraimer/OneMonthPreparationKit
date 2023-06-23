def sumXOR(n):
    #...
    count = 0

    while n != 0: #enters the loop until encounter is not equal to 0
        if n % 2 == 0: # check reminder is equal to 0 if yes
            count += 1 #if yes then incriment count varaiable by one
        n //= 2 #divide n by 2 effectively shifting its binary representation one bit to the right

    return 2**count #return 2**count after exiting the loop return 2 raised to power of count

n = int(input().strip())

result = sumXOR(n)

print(result)
