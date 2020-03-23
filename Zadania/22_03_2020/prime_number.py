# Square.py

number = int(input("Podaj liczbe\n"))
is_prime = True

for counter in range(2, number - 1):
    result = number % counter
    if result == 0:
        is_prime = False
        break
    counter += 1

print(is_prime)