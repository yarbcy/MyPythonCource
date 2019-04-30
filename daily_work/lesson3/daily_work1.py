a = set("112233444")
#print(a)


a = frozenset('11112222233333444')
#print(a) 

print(a.__doc__)

#bool = true 
#int =12
# float = 12.5
# list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
# tuple = ( 'abcd', 786 , 2.23, 'john', 70.2 )
# str = “My name is …”
# set = set('qwerty') => set(['e', 'q', 'r', 't', 'w', 'y'])frozenset = frozenset('qwerty')dict = {'name': 'john',‘id':6734, ‘role': ‘admin'}

# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# %.<number of digits>f - Floating point numbers with a fixed amount of digits to the right of the dot.
# %x/%X - Integers in hex representation (lowercase/uppercase)

# # default(implicit) order
# default_order = "{}, {} and {}".format('John','Bill','Sean')
# # order using positional argument
# positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
# # order using keyword argument
# keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
# >>> # formatting integers
# >>> "Binary representation of {0} is {0:b}".format(12)
# 'Binary representation of 12 is 1100'
# >>> # formatting floats
# >>> "Exponent representation: {0:e}".format(1566.345)
# 'Exponent representation: 1.566345e+03'
# >>> # round off
# >>> "One third is: {0:.3f}".format(1/3)
# 'One third is: 0.333'

list = ['111','222']

if '222' in list:
    print('+')

