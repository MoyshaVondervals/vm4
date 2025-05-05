import math

from methods.LinearApproximation import linearApproximation


def logarithmicApproximations(matrix):
    x = matrix[1]
    y = matrix[2]
    n = len(x)
    ln_x = [math.log(xi) for xi in x]
    newMatrix = [matrix[0], ln_x, y]
    coeffs = linearApproximation(newMatrix, n)
    return coeffs
