#----------------------------ПУЗЫРЁК-----------------------
for i in range(len(mass)-2):
    for j in range(len(mass)-i-1):
        if mass[j] > mass[j+1]:
            mass[j],mass[j+1] = mass[j+1],mass[j]
print(mass)

#--------------------------ВСТАВКИ-------------------------
for i in range(1,len(mass)):
    temp = mass[i]
    j = i - 1
    while (j >= 0) and (mass[j] > temp):
        mass[j+1] = mass[j]
        j -= 1
    mass[j+1] = temp
print(mass)

#--------------УЛУЧШЕННЫЕ ВСТАВКИ-------------------------
mass.insert(0,0)
for i in range(2,len(mass)):
    mass[0] = mass[i]
    j = i - 1
    while mass[j] > mass[0]:
        mass[j+1] = mass[j]
        j -= 1
    mass[j+1] = mass[0]
print(mass[1:])

#--------------------БИНАРНЫЕ ВСТАВКИ--------------------
for i in range(1,len(mass)):
    if mass[i-1] > mass[i]:
        temp = mass[i]
        left = 0
        right = i-1
        while left < right:
             centr = (left+right)//2
             if mass[centr] < temp:
                 left = centr + 1
             if mass[centr] >= temp:
                 right = centr - 1
        for j in range(i-1,left-1,-1):
            mass[j+1] = mass[j]
        mass[left] = temp
print(mass)

#----------------ПРОСТОЙ ВЫБОР---------------------------
for i in range(len(mass)-1):
    min = mass[i]
    for j in range(i+1,len(mass)):
        if mass[j] < min :
            mini = j
    mass[i],mass[mini] = mass[mini],mass[i]
print(mass)

#---------------ШЕЛЛ------------------------------------
k = len(mass)//2
while k > 0:
    for i in range(len(mass)-k):
        while (i >= 0) and (mass[i] > mass[i+k]):
            mass[i],mass[i+k] = mass[i+k],mass[i]
            i -= 1
            print(mass)
    k = k//2
print(mass)

#---------------ШЕЙКЕР---------------------------------
left = 0
right = len(mass)-1
while left <= right:
    for i in range(left,right):
        if mass[i] > mass[i+1]:
            mass[i+1],mass[i] = mass[i],mass[i+1]
    right -= 1
    for i in range(right,left,-1):
        if mass[i-1] > mass[i]:
            mass[i-1],mass[i] = mass[i],mass[i-1]
    left += 1
print(mass)

#--------------QUICK SORT---------------------------
def quicksort(mass,left,right):
    i,j = left,right
    centr = left+(right-left)//2
    while i < j:
        while mass[i] < mass[centr]:
            i += 1
        while mass[j] > mass[centr]:
            j -= 1
        if i <= j:
            mass[i],mass[j] = mass[j],mass[i]
            i += 1
            j -= 1
    if left < j :
        quicksort(mass,left,j)
    if right > i:
        quicksort(mass,i,right)
    return(mass)

print(quicksort(mass,0,len(mass)-1))



