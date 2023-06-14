#Task Eleven
def birthday(s, d, m):
    #my no idea what is expecting from output as there is not sample of input and output
    count = 0
    for i in range(len(s)):
        if sum(s[i:i+m]) == d:
            count += 1
    return count

n = int(input().strip())

s = list(map(int, input().rstrip().split()))

first_multiple_input = input().rstrip().split()

d = int(first_multiple_input[0])

m = int(first_multiple_input[1])

result = birthday(s, d, m)

print(result)
