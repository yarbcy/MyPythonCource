import sys
try:
    value = int(input())
except:
    print()
    sys.exit()

if (value % 2) == 0:
    print('Value is odd')
else:
    print('Value is even')