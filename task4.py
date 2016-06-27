t = int(input())
for i in range(t):
    n = int(input())
    temp = list(map(int, input().split()))
    summleft = 0
    summrigth = 0
    for j in range(1, len(temp)):
        summrigth = summrigth + temp[j]
    for index in range(1, len(temp)):
        summleft = summleft + temp[index - 1]
        summrigth = summrigth - temp[index]
        # print(summleft,' ', summrigth)
        if (summrigth == summleft):
            print(1, end='')
            break
        if (summleft > summrigth):
            print(0, end='')
            break
