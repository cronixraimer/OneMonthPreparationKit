def caesarCipher(s, k):
    #...
    encrypted_text = ""

    #Iteration over character in the text

    for char in s:
        if char.isalpha():
            #Determine the appropriate shift based on the character's case
            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

                #Apple the shift and handle wrapping around the alphabet
            shifted_char = chr((ord(char) - base + k) % 26 + base)
            encrypted_text += shifted_char
        else:
            encrypted_text += char

    return encrypted_text

n = int(input().strip())

s = input()

k = int(input().strip())

result = caesarCipher(s, k)

print(result)
