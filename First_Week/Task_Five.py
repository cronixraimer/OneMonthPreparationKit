def lonelyinteg(a):
    unique_set = set()
    for i in a:
        if i not in unique_set:
            unique_set.add(i)
        else:
            unique_set.remove(i)
    unique_set = unique_set.pop()
    return unique_set


n = int(input().strip())
a = list(map(int, input().strip().split()))

result = lonelyinteg(a)
print(result)
