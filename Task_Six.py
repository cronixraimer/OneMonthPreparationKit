def flippingBits(n):
    rev = 1
    res = n
    for i in range(32):
        rem = res & rev
        res = res - rev if rem > 0 else res + rev
        rev = rev << 1
    return res

q = int(input().strip())

for i in range(q):
    n = int(input().strip())

    result = flippingBits(n)

print(n)
#No Idea how I have done this task but somehow I passed this one thanks to chaptgpt
