# Fibonacci.py

counter = int(input('Podaj ktora liczbe Fibonachiego wyswietlic\n'))
number_1 = 0
number_2 = 1
result = 0
for i in range (0, counter):
    result = number_1 + number_2
    number_1 = number_2
    number_2 = result

print(number_1)