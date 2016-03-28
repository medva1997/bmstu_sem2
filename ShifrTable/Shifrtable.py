

def rotate(Tb,N):
    for i in range(0,N//2):
        for j in range(i,N-1-i):
             tmp = Tb[i][j]
             Tb[i][j] = Tb[n-j-1][i]
             Tb[n-j-1][i] = Tb[n-i-1][n-j-1]
             Tb[n-i-1][n-j-1] = Tb[j][n-i-1]
             Tb[j][n-i-1] = tmp
    return Tb

def PrintTable(Tb,N):
    for i in range(N):
        for j in range(N):
            print(Tb[i][j], end="\t")
        print()
    print()

def shifravanie(mask,out,sent,k):
    for i in range(n):
        for j in range(n):
            if (mask[i][j] == 1):
                out[i][j] = sent[k]
                k += 1
    return out,k


import random
n = int(input("Введите размер шифровальной таблицы: "))
Table = []
for i in range(n):
    Table.append([])
    for j in range(n):
        Table[i].append(0)

c = 1
for i in range(n // 2):
    for j in range(n // 2):
        Table[i][j] = c
        Table[j][n - i - 1] = c
        Table[n - i - 1][n - j - 1] = c
        Table[n - j - 1][i] = c
        c = c + 1
c = c - 1

block = []

while (len(block) != (n // 2) ** 2):
    i = random.randint(0, n - 1)
    j = random.randint(0, n - 1)
    flag = True
    for k in range(len(block)):
        if (Table[i][j] == -1) or (Table[i][j] == block[k]):
            flag = False
            break
    if (flag == True):
        block.append(Table[i][j])
        Table[i][j] = -1

for i in range(n):
    for j in range(n):
        if (Table[i][j] != -1):
            Table[i][j] = 0
        else:
            Table[i][j] = 1

PrintTable(Table,n)

key = []

for i in range(n):
    m = 0
    for j in range(n):
        m += Table[i][j] * 2 ** (n - j - 1)
    key.append(m)

print()

sentense = "катятымолодецтеперьтызнаешьипрекраснопонимаешькакустроенэтотшифр"
print(len(sentense))
k = 0

Shifr = []
for i in range(n):
    Shifr.append([])
    for j in range(n):
        Shifr[i].append(0)

Shifr,k=shifravanie(Table,Shifr,sentense,k)
Table=rotate(Table,n)
Shifr,k=shifravanie(Table,Shifr,sentense,k)
Table=rotate(Table,n)
Shifr,k=shifravanie(Table,Shifr,sentense,k)
Table=rotate(Table,n)
Shifr,k=shifravanie(Table,Shifr,sentense,k)
Table=rotate(Table,n)

PrintTable(Table,n)
PrintTable(Shifr,n)

print()
print(key)
