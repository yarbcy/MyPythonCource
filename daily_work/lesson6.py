# def function():
#     """This documment current function"""
#     pass

# print(function.__doc__)

# def print_info(age,name):
#     print(age,name)

# print_info(name='Bohdan', age=33)

# def print_info(name,age=33):
#     print(age,name)

# print_info('Bohdan')

# name = 0

# def print_info(name=3,*vartuple):
#     print(name)
#     for var in vartuple:
#         print(var)

# print_info(10,'aaa',12,13)

# def calcFactorial(x):
#     if x ==1:
#         return 1
#     else:
#         return (x * calcFactorial(x-1))

# print(calcFactorial(5))

# # Lambda functions
# double = lambda x: x*2

# print(double(5))


# def function(*args):
#     print(args)
#     return 1


# print(function(111,'444'))


# def function(**kwargs):
#     return kwargs


# print(function(111,'444'))

# g = lambda x: x*2

# print(g(5))

# g = lambda x: x*2

# print((lambda x: x*3)(3))

# 1
# def calculateAvarageSum(*args):
#     count = 0
#     sum = 0
#     for arg in args:
#         sum += float(arg)
#         count += True
#     return sum / count

# print(calculateAvarageSum(5,7,8,9,11,777))
# 2
# def _abs(x):
#     return abs(x)

# print(_abs(-1000))
#3
# def minMax(n=3,m=5):
#     """ This function compares two values """
#     if n > m:
#         return n
#     elif n==m:
#         return 0
#     else:
#         return m

# print(minMax(7,m=100), minMax.__doc__) 

#4
def calculateRectangle(a=2,b=5):
    return (a * b) * 2

def calculateCircle(radius=3):
    return (3.14 * radius)*(3.14 * radius)

def calculateTriangle(a=2,b=5):
    return (a * b)

def calculateAndPrint():
    choise = float(input('Choise 1 - calculateRectangle(), 2 - calculateCircle(), 3 - calculateTriangle()'))

    if choise == 1:
        print(calculateRectangle())

    if choise == 2:
        print(calculateCircle())

    if choise == 3:
        print(calculateTriangle())

calculateAndPrint()


    


















