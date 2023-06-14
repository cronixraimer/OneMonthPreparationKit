import string

def pangrams(s):
    #pangrams task will be contined tomorrow!mmm
    #counts = {}
    #res = []
    #Creating a set of valid alphabet characters
    #valid_alphabet = set(alphabet)

    #Iterating over the characters in the sentence
    #for i in s:
        #Checking if the characters is a valid character in the valid_alphabet
        #if i in valid_alphabet:
        #    if i in counts:
        #        counts[i] += 1
        #    else:
        #        counts[i] = 1

    #for i in alphabet:
    #    if i in counts:
    #        res.append("Pangrams")
    #    else:
    #        res.append("Not Pangrams")

    #return res

    alphabet = set(string.ascii_lowercase)
    sentence_letters = set(s.lower())

    return alphabet.issubset(s.lower())





s = input().strip()
#alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
#'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#result = pangrams(s)
if pangrams(s):
    print("pangram")
else:
    print("not pangram")
#print(result)
