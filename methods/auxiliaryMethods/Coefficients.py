import math


def pirson(matrix):
    n = len(matrix[0])
    xAvr = sum(matrix[1])/n
    yAvr = sum(matrix[2])/n
    numerator = 0
    denominatorL=0
    denominatorR = 0
    for i in range(len(matrix[0])):
        numerator+= (matrix[1][i]-xAvr)*(matrix[2][i]-yAvr)
        denominatorL += (matrix[1][i]-xAvr)**2
        denominatorR += (matrix[2][i]-yAvr)**2

    r = round((numerator)/(math.sqrt(denominatorL*denominatorR)), 6)
    code = getPirsonCode(r)
    return code, r

def getPirsonCode(r):
    if 0<abs(r)<=0.3:
        return 31
    elif 0.3<abs(r)<=0.5:
        return 32
    elif 0.5<abs(r)<=0.7:
        return 33
    elif 0.7<abs(r)<=0.9:
        return 34
    elif 0.9<abs(r)<=1:
        return 35

def getRowIndex(n):

    return (n*2) +1


def standardDeviation(S, n):
    sigma = round(math.sqrt(S/n), 6)
    return sigma

def determination(matrix, c):
    avrFi = sum(matrix[getRowIndex(c)])/(len(matrix[0]))
    numerator = 0
    denominator = 0
    for i in range(len(matrix[0])):
        numerator+= (matrix[2][i]-matrix[getRowIndex(c)][i])**2
        denominator += (matrix[2][i]-avrFi)**2
    r2 = round(1-(numerator/denominator), 6)
    code = getDetCode(r2)
    return code, r2

def getDetCode(r):
    if r<=0.5:
        return 41
    elif 0.5<r<=0.75:
        return 42
    elif 0.75<r<=0.95:
        return 43
    elif 0.95<r:
        return 44