import math

def counterGame(n):
    #...
    count = 0
    while n >  1:
        # Check if n is a power of 2
        if n & (n - 1) == 0:
            n //= 2
        else:
            #Find the largest power of 2 less than n and substracting it from n and updating n

                n = n - 2 ** math.trunc(math.log2(n))

        count += 1

    if count % 2 == 0:
        return "Richard"
    else:
        return "Louise"



t = int(input().strip())

for i in range(t):
    n = int(input().strip())

    result = counterGame(n)

    print(result)
