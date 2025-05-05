from sympy import false

from utils.Utils import addLinear, addQuadratic, addCubic, addLogarithmic, addPower, addExponential


def addDotsToMatrix(matrix, linear, quadratic, cubic):
    validX = False
    validY = False

    lin = []
    linS = []
    quad = []
    quadS = []
    cub = []
    cubS = []

    exp = []
    expS = []
    log = []
    logS = []
    pow = []
    powS = []

    sumS = []
    countX = 0
    countY = 0
    for i in range(len(matrix[1])):
        lin.append(addLinear(linear, matrix[1][i]))
        linS.append((addLinear(linear, matrix[1][i])-matrix[2][i])**2)
        quad.append(addQuadratic(quadratic, matrix[1][i]))
        quadS.append((addQuadratic(quadratic, matrix[1][i]) - matrix[2][i]) ** 2)
        cub.append(addCubic(cubic, matrix[1][i]))
        cubS.append((addCubic(cubic, matrix[1][i]) - matrix[2][i]) ** 2)
        if matrix[1][i]>0:
            countX += 1
        if matrix[2][i]>0:
            countY += 1



    matrix.append(lin)
    matrix.append(linS)
    sumS.append(round(sum(linS), 6))
    matrix.append(quad)
    matrix.append(quadS)
    sumS.append(round(sum(quadS), 6))
    matrix.append(cub)
    matrix.append(cubS)
    sumS.append(round(sum(cubS), 6))

    if countX == countY == len(matrix[0]):
        for i in range(len(matrix[0])):
            pow.append(addPower(matrix, matrix[1][i]))
            powS.append((addPower(matrix, matrix[1][i]) - matrix[2][i]) ** 2)
        matrix.append(pow)
        matrix.append(powS)
        sumS.append(round(sum(powS), 6))
        validX = True
        validY = True




    if countX==len(matrix[0]):
        for i in range(len(matrix[0])):
            log.append(addLogarithmic(matrix, matrix[1][i]))
            logS.append((addLogarithmic(matrix, matrix[1][i]) - matrix[2][i]) ** 2)
        matrix.append(log)
        matrix.append(logS)
        sumS.append(round(sum(logS), 6))
        validX = True


    if countY==len(matrix[0]):
        for i in range(len(matrix[0])):
            exp.append(addExponential(matrix, matrix[1][i]))
            expS.append((addExponential(matrix, matrix[1][i]) - matrix[2][i]) ** 2)
        matrix.append(exp)
        matrix.append(expS)
        sumS.append(round(sum(expS), 6))
        validY = True


    return sumS, matrix, validX, validY


