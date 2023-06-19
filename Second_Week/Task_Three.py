def pageCount(n, p):

    backward = (n + 2) // 2 - 1
    forward = (p + 2) // 2 - 1
    return min(forward, backward - forward)


n = int(input().strip())

p = int(input().strip())

result = pageCount(n, p)

print(str(result))

#    count = 0
#
#    if n == p:
#        count = n - p
#        return count
#    diff = abs(n - p)
#    if diff > p:
#        page = abs(n - diff)
#        count = page // 2
#    else:
#        count = diff // 2
#    return count
