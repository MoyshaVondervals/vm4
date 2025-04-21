import math

from utils.Utils import predefined_functions


def matrixIXY(eq_num, left_bound, right_bound, h):
    matrix = []
    iArr = []
    XiArr = []
    YiArr = []
    steps = int(math.floor(round((right_bound-left_bound)/h, 6)))+1
    if not(8<=steps<=12):
        return 0, []

    f = predefined_functions[eq_num].function
    validPoints = 0
    for i in range(steps):
        if checkExistence(eq_num, left_bound+i*h):
            validPoints += 1
            iArr.append(i+1)

            XiArr.append(round(left_bound+i*h, 6))
            YiArr.append(round(f(left_bound+i*h), 6))
        else:
            return 0, []

    matrix.append(iArr)
    matrix.append(XiArr)
    matrix.append(YiArr)
    return steps, matrix

def checkExistence(eq_num, x):
    f = predefined_functions[eq_num].function
    try:
        val = f(x)
        if isinstance(val, complex):
            return False
        return True
    except (ZeroDivisionError, OverflowError, ValueError):
        return False
