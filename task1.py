n = int(input())
for i in range(n):
    m, n = map(int, input().split())
    mem = 0

    temp = list(map(int, input().split()))
    for j in range(len(temp)):
        if (temp[j] <= 0):
            mem = mem + 1
    if mem < n:
        print(1)
    else:
        print(0)
