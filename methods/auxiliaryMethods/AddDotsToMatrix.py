from sympy import false

from utils.Utils import addLinear, addQuadratic, addCubic, addLogarithmic, addPower, addExponential


def addDotsToMatrix(matrix, linear, quadratic, cubic):
    limitation = False

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
    count = 0
    for i in range(len(matrix[1])):
        lin.append(addLinear(linear, matrix[1][i]))
        linS.append((addLinear(linear, matrix[1][i])-matrix[2][i])**2)
        quad.append(addQuadratic(quadratic, matrix[1][i]))
        quadS.append((addQuadratic(quadratic, matrix[1][i]) - matrix[2][i]) ** 2)
        cub.append(addCubic(cubic, matrix[1][i]))
        cubS.append((addCubic(cubic, matrix[1][i]) - matrix[2][i]) ** 2)
        if matrix[1][i]>0:
            count += 1
            exp.append(addExponential(linear, matrix[1][i]))
            expS.append((addExponential(linear, matrix[1][i]) - matrix[2][i]) ** 2)
            log.append(addLogarithmic(linear, matrix[1][i]))
            logS.append((addLogarithmic(linear, matrix[1][i]) - matrix[2][i]) ** 2)
            pow.append(addPower(linear, matrix[1][i]))
            powS.append((addPower(linear, matrix[1][i]) - matrix[2][i]) ** 2)



    matrix.append(lin)
    matrix.append(linS)
    sumS.append(round(sum(linS), 6))
    matrix.append(quad)
    matrix.append(quadS)
    sumS.append(round(sum(quadS), 6))
    matrix.append(cub)
    matrix.append(cubS)
    sumS.append(round(sum(cubS), 6))
    if count==len(matrix[1]):
        matrix.append(exp)
        matrix.append(expS)
        sumS.append(round(sum(expS), 6))
        matrix.append(log)
        matrix.append(logS)
        sumS.append(round(sum(logS), 6))
        matrix.append(pow)
        matrix.append(powS)
        sumS.append(round(sum(powS), 6))
    else:
        limitation = True

    return sumS, matrix, limitation


