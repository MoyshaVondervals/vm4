from methods.auxiliaryMethods.Kramer import findCoeffs
from utils.Utils import predefined_functions


def quadraticApproximation(eq_num, matrix, n):
    f = predefined_functions[eq_num].function
    sx = round(sum(matrix[1]), 6)
    sxx=0
    sxxx = 0
    sxxxx = 0

    sy = round(sum(matrix[2]), 6)
    sxy = 0
    sxxy = 0
    for i in range(len(matrix[0])):
        sxx+=matrix[1][i]**2
        sxxx+=matrix[1][i]**3
        sxxxx+=matrix[1][i]**4

        sxy+=matrix[1][i]*matrix[2][i]
        sxxy+=matrix[1][i]**2 * matrix[2][i]
    sxx = round(sxx, 6)
    sxxx = round(sxxx, 6)
    sxxxx = round(sxxxx, 6)
    sxy = round(sxy, 6)
    sxxy = round(sxxy, 6)




    coeffs = findCoeffs(
        [
            [n, sx, sxx],
            [sx, sxx, sxxx],
            [sxx, sxxx, sxxxx],
        ],
        [sy, sxy, sxxy]
    )

    return coeffs