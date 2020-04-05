"""
Napisz funkcje wykorzystująca metodę Euklidesa 
znajdującą wspólny czynnik dwóch liczb. 
Powinna ona działać w taki sposób:

1. Masz dwie liczby, a i b,(podane z klawiatury)
2. Powtarzaj poniższe działania do momentu, aż b będzie równe zero:
przypisz do a wartość b
przypisz do b resztę z dzielenia a (przed zmiana) przez b (przed zmiana)
3. Zwróć ostatnia wartość a
"""
def calculate_gcd(number_1, number_2):
    if number_1 < number_2:
        number_1, number_2 = number_2, number_1
    while number_2 > 0:
        number_1, number_2 = number_2, number_1 % number_2
    return number_1

def gcd_for_n(*args):
    numbers = list(args)
    gcd_prime = numbers[0]
    for number in numbers:
        gcd_prime = calculate_gcd(gcd_prime, number)
    return gcd_prime

print(gcd_for_n(4, 6, 64, 128))
