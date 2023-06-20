def towerBreakers(n,m):
    #..

    if m == 1 or n % 2 == 0:
        return 2
    if n % 2 == 1:
        return 1
t = int(input().strip())

for i in range(t):
    first_mitiple_input = input().rstrip().split()

    n = int(first_mitiple_input[0])

    m = int(first_mitiple_input[1])

    result = towerBreakers(n, m)

    print(str(result))
