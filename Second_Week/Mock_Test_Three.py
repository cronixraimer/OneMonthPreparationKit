def anagram(s):
    #....
    n = len(s)
    if n % 2 != 0:
        return -1

    s1 = s[:n // 2]
    s2 = s[n // 2 :]

    rev_1 = {}
    rev_2 = {}

# Count the frequency of characters in the first and second halves of the string
    for i_1, i_2 in zip(s1, s2):
        rev_1[i_1] = rev_1.get(i_1, 0) + 1
        rev_2[i_2] = rev_2.get(i_2, 0) + 1

    count = 0
    
# Iterate over the unique characters in the combined string of s1 and s2
    for i in set(s1 + s2):
        count1 = rev_1.get(i, 0)
        count2 = rev_2.get(i, 0)
# Calculate the absolute difference in frequencies between s1 and s2
        count += abs(count1 - count2)

 # Divide the count by 2 to get the minimum number of characters to change
    return count // 2

q = int(input().strip())

for i in range(q):
    s = input()

    result = anagram(s)

    print(str(result))
