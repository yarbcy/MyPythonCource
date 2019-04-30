import sys
try:
    a = float(input())
    b = float(input())
except:
    print()
    sys.exit()
 
def evklid(a, b): # Функція знаходження найбільшого спільного дільника
    if a % b == 0:
        return b
    else:
        return evklid(b, a%b)
 
print (evklid(a, b))
 
nsk = a * b // evklid(a, b) # Знаходимо найменше спільне кратне// Цілочисельне ділення
print (nsk)