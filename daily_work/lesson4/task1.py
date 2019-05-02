
# count = 0
# while count < 100:
#     count += 2
#     print(count)

# for i in range(1,100,1):
#     if (i % 2) == 1:
#         print(i)
#         break
    

# list1 = list(range(1,100,1))

# for item in range(len(list1)):
#     list1[item] = float(list1[item])
# print(list1)

# fruits = ['banana','gfg','gbgg']
# print(list(enumerate(fruits)))


# FibArray = [0,1] 
  
# def fibonacci(n): 
#     if n<0: 
#         print("Incorrect input") 
#     elif n<=len(FibArray): 
#         return FibArray[n-1] 
#     else: 
#         temp_fib = fibonacci(n-1)+fibonacci(n-2) 
#         FibArray.append(temp_fib) 
#         return temp_fib 
  
# # Driver Program 

# input = 20
# for fib in range(1,input):  
#     print(fibonacci(fib)) 

list1 = []
for i in range(1,5):
    list1.append(i)

for i in range(len(list1)):
    print(list1[i], end="%")