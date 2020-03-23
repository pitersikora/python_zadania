# Square.py

number = int(input("Podaj liczbe\n"))
counter = 1
result = 1

while(result < number):
    result = counter * counter
    counter += 1

if result == number:
    print('TAK, liczba jest kwadratem innej liczby')
else:
    print('NIE')