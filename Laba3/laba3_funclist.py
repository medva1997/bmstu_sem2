import math
######################## f(x)=0 #####################################
def FuncZero(x):
    return 0

def ProizZero(x):
    return 0

def Proiz2Zero(x):
    return 0

def Proiz3Zero(x):
    return 0

######################## f(x)=0.02*x*x-4 #####################################
def Func(x):
    return 0.02 * x * x - 4


def ProizF(x):
    return 0.02 * 2 * x

def Proiz2F(x):
    return 0.04

def Proiz3F(x):
    return 0.0

######################## f(x)=sinx #####################################
def Func1(x):
    return math.sin(x)

def ProizF1(x):
    return math.cos(x)

def Proiz2F1(x):
    return -math.sin(x)

def Proiz3F1(x):
    return -math.cos(x)

######################## f(x)=cos(x) #####################################
def Func4(x):
    return math.cos(x)

def ProizF4(x):
    return math.sin(x)

def Proiz2F4(x):
    return -math.cos(x)

def Proiz3F4(x):
    return math.sin(x)

######################## f(x)=sinx/x #####################################
def Func2(x):
    if x == 0:
        return 1.0
    return math.sin(x) / x

def ProizF2(x):
    if x == 0:
        return 0.0
    return (x * math.cos(x) - math.sin(x)) / (x * x)

def Proiz2F2(x):
    if (x == 0):
        return 1
    return 2 * math.sin(x) / x ** 3 - 2 * math.cos(x) / x ** 2 - math.sin(x) / x

def Proiz3F2(x):
    if (x == 0):
        return 1
    return -6*math.sin(x)/(x**4)+6*math.cos(x)/(x**3)+3*math.sin(x)/(x**2)-math.cos(x)/x


######################## f(x)=-sinx+1.5 #####################################

def Func3(x):
    return -math.sin(x) + 1.5

def ProizF3(x):
    return -math.cos(x)

def Proiz2F3(x):
    return math.sin(x)

def Proiz3F3(x):
    return math.cos(x)
