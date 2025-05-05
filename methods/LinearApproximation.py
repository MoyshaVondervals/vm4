import numpy as np

from methods.auxiliaryMethods.Kramer import findCoeffs


def linearApproximation(matrix, n):
    sx = round(sum(matrix[1]), 6)
    sy = round(sum(matrix[2]), 6)
    sxx=0
    sxy=0
    for i in range(len(matrix[0])):
        sxx+=matrix[1][i]**2
        sxy+=matrix[1][i]*matrix[2][i]
    sxx = round(sxx, 6)
    sxy = round(sxy, 6)


    coeffs = findCoeffs(
        [
            [n, sx],
            [sx, sxx]
        ],
        [sy, sxy]
    )
    return coeffs



