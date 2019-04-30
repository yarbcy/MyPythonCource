import sys
try:
    first = float(input())
    second = float(input())
except:
    print()
    sys.exit()

if first > second:
    print('First is bigger')
elif first == second:
    print('First is equal second')
else:
    print('Second is bigger')

