import  numpy as np
# Арифметические операции
for i in range(1,15):
    print('\n')

print('вормирование исходных массивов')

a=np.arange(1,5).reshape(2,2)
b= np.arange(5,9).reshape(2,2)
print(a)
print(b)

print('+')
c_plus=a+b
print(c_plus)

print('-')
c_minis=a-b
print(c_minis)


print(' * by ell')
c_mult=a*b
print(c_mult)


print('pow')
c_power=a**b
print(c_power)

print('* на число')
c_num=a*5
print(c_num)

print('Матричное умножение 2*2')
c_multmat=np.dot(a,b)
print(c_multmat)

print('Матричное умножение 2*3')
x=np.arange(1,7).reshape(2,3)
a_x=np.dot(a,x)
print(a_x)

print("деление на 0")
a0=np.arange(0,4).reshape(2,2)
a_div=a/a0
print(a_div)


print("остаток  на деление")
a_remainder=a%a0
print(a_remainder)


a_div=a/a0
print(a_div)

d=np.add(a,b)
print(d)

