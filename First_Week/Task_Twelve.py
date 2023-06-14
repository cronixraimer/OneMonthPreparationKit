#Task twelve is considered to finding mistake and aimed for XOR
#also condition was you can edit the code only 3 times
def strings_xor(s, t):
    res = ""
    for i in range(len(s)):
        if s[i] == t[i]: #first mistake was here if s[i] = t[i] it was bug as is has to be equal if s[i] == t[i] seems to be True

            res += '0'; #second mistake was here as it was res = '0' but it should iterate not creating empty res += '0'

        else:
            res += '1'; #third mistake was same as second one as it was mistaken on iteration of strings_xor
            

    return res

s = input()
t = input()
print(strings_xor(s, t))
