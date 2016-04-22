
def rotate(Tb,N):
    for i in range(0,N//2):
        for j in range(i,N-1-i):
             tmp = Tb[i][j]
             Tb[i][j] = Tb[n-j-1][i]
             Tb[n-j-1][i] = Tb[n-i-1][n-j-1]
             Tb[n-i-1][n-j-1] = Tb[j][n-i-1]
             Tb[j][n-i-1] = tmp
    return Tb


def povorot(A,n):
	for in in range(A):
		for i in range(len(A[i])):


def PrintTable(Tb,N):
    for i in range(N):
        for j in range(N):
            print(Tb[i][j], end="\t")
        print()
    print()


key = [32, 8, 8, 20, 129, 70, 10, 99]


A=[[0]*len(key) for i in range(len(key))]
for i in range(len(key)):
	k=len(key)-1
	p=0
	while key[i]!=0:
		if key[i]>=2**(k-p):
			#print(p)
			key[i]=key[i]-2**(k-p)
			A[i][p]=1
		p+=1
	print(*A[i])


stroka='ракекснуроьпастртонотеиымнэязттаынеошаемтошььлошипркдиефецткраеп'
Table=[]
k=0
n=len(key)

for i in range(n):
    Table.append([])
    for j in range(n):
        Table[i].append(0)

for i in range(n):
    for j in range(n):
        Table[i][j]=stroka[k]
        k+=1

PrintTable(Table,n)
outtext=''
for m in range(4):

	for i in range(n):
	    for j in range(n):
	    	if(A[i][j]==1):
	    		outtext+=Table[i][j]
	A=rotate(A,n)


print(outtext)


