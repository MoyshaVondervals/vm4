from methods.auxiliaryMethods.Kramer import findCoeffs


def cubicApproximation(matrix, n):

    sx = round(sum(matrix[1]), 6)
    sxx=0
    sxxx = 0
    sxxxx = 0
    sxxxxx = 0
    sxxxxxx = 0

    sy = round(sum(matrix[2]), 6)
    sxy = 0
    sxxy = 0
    sxxxy = 0
    for i in range(len(matrix[0])):
        sxx+=matrix[1][i]**2
        sxxx+=matrix[1][i]**3
        sxxxx+=matrix[1][i]**4
        sxxxxx+=matrix[1][i]**5
        sxxxxxx+=matrix[1][i]**6

        sxy+=matrix[1][i]*matrix[2][i]
        sxxy+=matrix[1][i]**2 * matrix[2][i]
        sxxxy+=matrix[1][i]**3 * matrix[2][i]
    sxx = round(sxx, 6)
    sxxx = round(sxxx, 6)
    sxxxx = round(sxxxx, 6)
    sxxxxx = round(sxxxxx, 6)
    sxxxxxx = round(sxxxxxx, 6)
    sxy = round(sxy, 6)
    sxxy = round(sxxy, 6)
    sxxxy = round(sxxxy, 6)




    coeffs = findCoeffs(
        [
            [n, sx, sxx, sxxx],
            [sx, sxx, sxxx, sxxxx],
            [sxx, sxxx, sxxxx, sxxxxx],
            [sxxx, sxxxx, sxxxxx, sxxxxxx]
        ],
        [sy, sxy, sxxy, sxxxy]
    )

    return coeffs