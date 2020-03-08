# Equation

import math

print('Jakiego typu rownanie chcesz policzyc ? \n 1. liniowe\n 2. Kwadratowe\n Wpisz nr opcji:')
option = input()

if option == '1':
    print('Wybrano rownanie liniowe ax + b = 0')
    a = int(input('Podaj a\n'))
    b = int(input('Podaj b\n'))
    if a == 0:
        if b == 0:
            print('Rownanie tozsamosciowe - x nalezy do zbioru liczb rzeczywistych')
            exit(0)
        else:
            print('Rownanie sprzeczne - brak rozwiazan')
            exit(0)
    result = -1 * b / a
    print("Wynik rownania liniowego to: %f" % result)
    print("Sprawdzenie: %f * %f + %f = %f + %f = %f" % (a, result, b, result * a, b, result * a + b))

if option == '2':
    print('Wybrano rownanie kwadratowe ax^2 + bx + c = 0')
    a = int(input('Podaj a\n'))
    b = int(input('Podaj b\n'))
    c = int(input('Podaj c\n'))
    delta = b**2 - (4 * a * c)

    if delta < 0:
        print('Delta ujemna - rownanie nie ma rozwiazan')
        exit(0)
    elif delta == 0:
        print('Delta rowna 0 - rownanie ma dokladnie jedno rozwiazanie')
        result = -1 * b / (2 * a)
        print("Pierwiastek rownania kwadratowego to: %f" % result)
        print("Sprawdzenie: %f * %f ^ 2 + %f * %f + %f = %f" % (a, result, b, result, c, a * (result ** 2) + b * result + c))
    else:
        print('Delta wieksza niz 0 - rownanie ma dokladnie dwa rozwiazania')
        result_1 = (-1 * b + math.sqrt(delta)) / (2 * a)
        result_2 = (-1 * b - math.sqrt(delta)) / (2 * a)
        print("Pierwiastki rownania kwadratowego to: %f oraz % f" % (result_1, result_2))
        print("Sprawdzenie dla x1: %f * %f ^ 2 + %f * %f + %f = %f" % (a, result_1, b, result_1, c, a * (result_1 ** 2) + b * result_1 + c))
        print("Sprawdzenie dla x2: %f * %f ^ 2 + %f * %f + %f = %f" % (a, result_2, b, result_2, c, a * (result_2 ** 2) + b * result_2 + c))