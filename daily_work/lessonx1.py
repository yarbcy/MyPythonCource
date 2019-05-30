# arr1 = [1,2,3]
# arr2 = [4,5,6]

# zipped = [u*v for u, v in zip(arr1,arr2)]

# print(zipped)

# str1 = 'abcdf'
# t = (1,2,3)

# print(dict(zip(str1,t)))
# print(list(zip(str1,t)))

# for i in list(zip(str1,t)):
#     print(i)

# s = 'abcd'
# t = [10,20,30]

# g = [(s[i],t[i]) for i in range(len(s)-1)]

# print(g)

# result = list(map(lambda n: 3*n, t))
# print(result)
# def isPos(number):
#     return number > 0

# a = [-1,2,-3,4,-5,6,-7,8,-9,10]
# r = filter(lambda n: not isPos(n), a)
# print(list(r))

# from functools import reduce

# sentences = ['capitan America', 'capitan Jak', 'capitan']
# cap_count = reduce(lambda a, x: a + x.count('capitan'), sentences, 0)
# print(cap_count)

# def f(x,y):
#     return x*y

# a = [1,2,3]
# b = [4,5,6]

# print(list(map(f,a,b)))

# g = (x*x+1 for x in range(1,11))

# print(list(g))

# def myGen():
#     yield 'a'
#     yield 'b'
#     yield 'c'

# # for i in myGen():
# #     print(i)
# print(next(myGen()))
# print(next(myGen()))

# l = [1,2,3]
# i = iter(l)

# print(next(i))
# print(next(i))
# print(next(i))

# def smart_divide(func):
#    def inner(a,b):
#       print("I am going to divide",a,"and",b)
#       if b == 0:
#          print("Whoops! cannot divide")
#          return

#       return func(a,b)
#    return inner

# @smart_divide
# def divide(a,b):
#     return a/b

# print(divide(2,0))

# 1.  Спробуйте переписати наступний код через map. Він приймає список реальних імен і замінює їх прізвищами, використовуючи  більш надійний метод.

# names = ['Sam', 'Don', 'Daniel'] 
# for i in range(len(names)): 
#     names[i] = hash(names[i]) 
# print(names)

# names = ['Sam', 'Don', 'Daniel'] 
# print(list(map(lambda n: hash(n), names)))

# def isPos(number):
#     return number > 0

# aaa = ['red', 'green', 'black', 'red', 'brown', 'red', 'blue', 'red', 'red', 'yellow']
# r = filter(lambda n: n =='red', aaa)

# print(list(r))

# sss = ['1','2','3','4','5','6','7']
# sss1 = []
# for i in sss:
#     sss1.append(int(i))
# print(sss1)

# sss2 = list(map(lambda n: int(n), sss))
# print(sss2)

mile = [2,3,4,5,6,7,8]

print(list(map(lambda n: n*1.6,mile)))





