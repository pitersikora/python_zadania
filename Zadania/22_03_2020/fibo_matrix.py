# fibo_matrix.py

def multiply_matrix(m1, m2):
    product = [[0,0], [0,0]]
    product[0][0] = m1[0][0] * m2[0][0] + m1[0][1] * m2[1][0]
    product[0][1] = m1[0][0] * m2[0][1] + m1[0][1] * m2[1][1]
    product[1][0] = m1[1][0] * m2[0][0] + m1[1][1] * m2[1][0]
    product[1][1] = m1[1][0] * m2[0][1] + m1[1][1] * m2[1][1]
    return product

def fast_matrix_power(base_matrix, exponent):
    if exponent == 1:
        return base_matrix
    elif exponent % 2 == 0:
        return fast_matrix_power(multiply_matrix(base_matrix, base_matrix), exponent / 2)
    else:
        return multiply_matrix(fast_matrix_power(multiply_matrix(base_matrix, base_matrix), (exponent - 1) / 2), base_matrix)

def calculate_fibo(which_fibonacci_number):
    result = [[1,1], [1,0]]
    return fast_matrix_power(result, which_fibonacci_number)[0][1]


counter = int(input('Podaj ktora liczbe Fibonachiego wyswietlic\n'))

print("%d Liczba z ciagu Fibonacciego to: %d" % (counter, calculate_fibo(counter)))