# Square.py

import math

number = input("Podaj liczbe\n")
number = math.sqrt(int(number))

if number.is_integer():
    print('Liczba jest kwadratem innej liczby, ta liczba to %d' % number)
else:
    print('Liczba nie jest kwadratem innej liczby')