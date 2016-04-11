import numpy as np
a=np.arange(12)
a1=np.copy(a)
print("Исходная матрица")
a2=np.reshape(a1,(3,4))
a2=a2.T
print('Транспонированая матрица')
print(a2,'\n')

#min,max,sum, сортировка
b=np.array([[2,8,0],[6,1,3],[4,7,5]])
print("\т Новая исходная матрица\n",b,'\n')

dsum=b.sum()
dmin=b.min()
dmax=b.max()

print("Некоторые значения для всей матрицы")
print('sum=',dsum,"min=",min,'max=',dmax,'\n')
mincol=b.min(axis=0)
maxrow=b.max(axis=1)
print('Значение min и max для стобцов и сток')
print('min в столбах=',mincol,'max  в строкахх= ',maxrow,'\n')