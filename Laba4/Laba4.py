import random,time,numpy
def Printer(id,out):
   #print('{:^85}'.format("Время выполнения сортировки"))
    #print()
    k='{:^24}'
    m='{:>7}'
    s1=s2=s3=''
    for i in range(len(out)//3):
        s1+=m.format(out[i])
    for i in range(len(out)//3,len(out)//3*2):
        s2+=m.format(out[i])
    for i in range(len(out)//3*2,len(out)):
        s3+=m.format(out[i])
    #print(k.format(" "),k.format("Упорядоченный"), k.format("Случайный"), k.format("Обратно упорядоченный"), sep='|' )
    print(k.format("Test "+str(id)),k.format(s1),k.format(s2),k.format(s3), sep='|')

def ShellSort(mas):
    def new_inc(mas):
        i=int(len(mas)/2)
        yield i
        while i!=1:
            if i==2:
                i=1
            else:
                i=int(numpy.round(i/2.2))
            yield i

    for inc in new_inc(mas):
        for i in range(inc,len(mas)):
            for j in range(i,inc-1,-inc):
                if mas[j-inc]<mas[j]:
                    break
                mas[j],mas[j-inc]=mas[j-inc],mas[j]
                #print(mas)

def shellSort(mas):
    def new_inc(mas):
        i=int(len(mas)/2)
        yield i
        while i!=1:
            if i==2:
                i=1
            else:
                i=int(numpy.round(i/2.2))
            yield i

    for inc in new_inc(mas):
        for i in range(inc,len(mas)):
            for j in range(i,inc-1,-inc):
                if mas[j-inc][2]<mas[j][2]:
                    break
                mas[j],mas[j-inc]=mas[j-inc],mas[j]
                #print(mas)

def work(id):

    out=[]
    for j in range(len(lenarr)):
        arr=[]
        for i in range(lenarr[j]):
            arr.append(i)
        start=time.time()
        ShellSort(arr)
        end=time.time()
        out.append(end-start)

    for j in range(len(lenarr)):
        arr=[]
        for i in range(lenarr[j]):
            arr.append(random.randint(1,9999999999))
        start=time.time()
        ShellSort(arr)
        end=time.time()
        out.append(end-start)

    for j in range(len(lenarr)):
        arr=[]
        for i in range(lenarr[j]):
            arr.append(lenarr[j]-i)
        start=time.time()
        ShellSort(arr)
        end=time.time()
        out.append(end-start)


    for i in range(len(out)):
        out[i]=int(out[i]*1000)
    #print(out)
    Printer(id,out)

def work1(id):
    out=[]
    for j in range(len(lenarr)):
        arr=[]
        for i in range(lenarr[j]):
            temp=[i,chr(i),i,i**2,chr(i)+chr(i+10)+chr(i+100)]
            arr.append(temp)
        start=time.time()
        shellSort(arr)
        end=time.time()
        out.append(end-start)

    for j in range(len(lenarr)):
        arr=[]
        for i in range(lenarr[j]):
            #arr.append(random.randint(1,9999999999))
            temp=[i,chr(i),random.randint(1,9999999999),chr(i)+chr(i+10)+chr(i+100)]
            arr.append(temp)
        start=time.time()
        shellSort(arr)
        end=time.time()
        out.append(end-start)

    for j in range(len(lenarr)):
        arr=[]
        for i in range(lenarr[j]):
            temp=[i,chr(i),lenarr[j]-i,i**2,chr(i)+chr(i+10)+chr(i+100)]
            arr.append(temp)            
        start=time.time()
        shellSort(arr)
        end=time.time()
        out.append(end-start)


    for i in range(len(out)):
        out[i]=int(out[i]*1000)
    #print(out)
    Printer(id,out)

lenarr=[1000,10000,100000]
k='{:^24}'

print()
print('{:^80}'.format("Сортировка Шелла"))
print("Время указано в миллисекундах")
print()
print(k.format(" "),k.format("Упорядоченный"), k.format("Случайный"), k.format("Обратно упорядоченный"), sep='|' )
work(1)
work(2)
work(3)
print("С дополнительной информацией")
work1(1)
work1(2)
work1(3)

print("Размеры массивов: ",*lenarr)

