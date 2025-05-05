import math

from methods.LinearApproximation import linearApproximation


def powerApproximations(matrix):
    x = matrix[1]
    y = matrix[2]
    n = len(x)
    ln_x = [math.log(xi) for xi in x]
    ln_y = [math.log(yi) for yi in y]
    newMatrix = [matrix[0], ln_x, ln_y]
    ln_a, b = linearApproximation(newMatrix, n)
    a = math.exp(ln_a)
    return [a, b]
