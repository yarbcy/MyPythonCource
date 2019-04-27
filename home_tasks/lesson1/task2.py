import sys


try:
    print('Please enter first number')
    first  = float(input('Enter first number: '))
    print('Please enter second number')
    second = float(input('Enter second number: '))
except:
    print('You entered non integer values. Exit from script.')
    sys.exit(True)

print(first + second)
print(first - second)