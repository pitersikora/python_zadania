# result: { ile_pierwiastkow: n, pierwiastki: (0, ..., n-1) }
import math

def pierwiaski_trojmianu(a, b, c):
    delta = b**2 - (4 * a * c)
    if delta < 0:
        return {"ile_pierwiastkow": 0, "pierwiastki": None}
        exit(0)
    elif delta == 0:
        return {"ile_pierwiastkow": 1, "pierwiastki": (-1 * b / (2 * a))}
        exit(0)
    else:
        result_1 = (-1 * b - math.sqrt(delta)) / (2 * a)
        result_2 = (-1 * b + math.sqrt(delta)) / (2 * a)
        return {"ile_pierwiastkow": 2 , "pierwiastki": (result_1, result_2)}
        exit(0)

#print(pierwiaski_trojmianu(2, 3, 2))
#print(pierwiaski_trojmianu(2, 2, -12))
#print(pierwiaski_trojmianu(2, 4, 2))
