n = int(input())
for i in range(n):
    lineone = input().lower()
    linetwo = input().lower()
    block = ["'", ' ', '.', ',', '!', '?']
    for i in range(len(block)):
        lineone = lineone.replace(block[i], '')
        linetwo = linetwo.replace(block[i], '')
    # print(lineone, ' ',linetwo)
    if (len(linetwo) == len(lineone)):
        a = set(lineone)
        b = set(linetwo)
        # print(a, '\n', b)
        if a == b:
            print(1)
        else:
            print(0)
    else:
        print(0)
