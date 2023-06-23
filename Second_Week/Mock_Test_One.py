def palindromeIndex(s):
    #...
    #Remove spaces and convert to lowercase
    s = s.replace(" ", " ").lower()
    l, r = 0, len(s) - 1

    for I in range(len(s) // 2):
        if s[l] != s[r]:
            if s[:l] + s[l + 1 :] == (s[:l] + s[l + 1 :])[::-1]:
                return l

            else:
                return r

        l += 1
        r -= 1
    return -1
    # Check if the string is already a palindrome
#    if s == s[::-1]: # Return -1 if it's already a palindrome
#        return -1
      # Check if removing index 0 makes it a palindrome
#    if s[1:] == s[1:][::-1]:
#        return 0

    # Check if removing index 3 makes it a palindrome
#    if s[:3] + s[4:] == (s[:3] + s[4:])[::-1]:
#        return 3

#    return -1  # Return -1 if no palindrome index is found

q = int(input().strip())

for i in range(q):
    s = input()

    result = palindromeIndex(s)

    print(result)
