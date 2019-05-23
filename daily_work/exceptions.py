# class CustomError(Exception):
#     def __init__(self,data):
#         self.data=data
#     def __str__(self):
#         return repr(self.data)



# try:
#     x
# except:
#     raise CustomError('error')
# finally:
#     exit

# class Figure:
#    def init(self, color):
#        self.color = color
      
#    def get_color(self):
#        return self.color

#    def info(self):
#        print("Figure")
#        print("Color: " + self.color)

# class Rectangle(Figure):
#    def init(self, color, width=100, height=100):
#        super().init(color)
#        self.width = width
#        self.height = height

#    def square(self):
#        return self.width * self.height

#    def info(self):
#        print("Rectangle")
#        print("Color: " + self.color)
#        print("Width: " + str(self.width))
#        print("Height: " + str(self.height))
#        print("Square: " + str(self.square()))

# fig1 = Figure('green')
# fig1.info()
# fig2=Rectangle("red",89,65)
# fig2.info()

# try:
#     value = int(input())
#     if value % 2 == 0:
#         print('Your value is odd')
#     if value % 2 == 1:
#         print('Your value is even')
# except:
#     raise print('PLease give me integer only')

# class NotValidAge(Exception):
#     def __init__(self,data):
#         self.data=data
#     def __str__(self):
#          return repr(self.data)

# try:
#     value = int(input('Please give me your age...'))
#     if value % 2 == 0:
#         print('Your age is odd')
#     if value % 2 == 1:
#         print('Your age is even')
#     if value < 0:
#         raise NotValidAge('NegativeNumber exception')

# except NotValidAge as e: 
#     print(e) 

try:
    string = input('enter two numbers comma separated')
    firstValue = float(string[0])
    secondValue = float(string[1])
    print(firstValue/secondValue)
except:
    raise print('Enter integer not string')
else:
    print('No exceptions')
finally:
    print('Your code excuted')
