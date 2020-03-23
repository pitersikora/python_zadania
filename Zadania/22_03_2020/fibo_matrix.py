# fibo_matrix.py

def multiply_matrix(matrix1, matrix2):
    product = [[0,0], [0,0]]

    product[0][0] = matrix1[0][0] * matrix2[0][0] + matrix1[0][1] * matrix2[1][0]
    product[0][1] = matrix1[0][0] * matrix2[0][1] + matrix1[0][1] * matrix2[1][1]
    product[1][0] = matrix1[1][0] * matrix2[0][0] + matrix1[1][1] * matrix2[1][0]
    product[1][1] = matrix1[1][0] * matrix2[0][1] + matrix1[1][1] * matrix2[1][1]

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