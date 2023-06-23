def getTotalX(a, b):
    #.....
    max_a = max(a)
    min_b = min(b)
    count = 0

    for num in range(max_a, min_b + 1):
        if all(num % factor == 0 for factor in a) and all(factor % num == 0 for factor in b):
            count += 1

    return count



first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

brr = list(map(int, input().rstrip().split()))

total = getTotalX(arr, brr)

print(str(total))
