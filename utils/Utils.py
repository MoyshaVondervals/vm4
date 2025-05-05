import math
from audioop import error
from collections.abc import Callable

import numpy as np

from methods.ExponentialApproximation import exponentialApproximation
from methods.LinearApproximation import linearApproximation
from methods.LogarithmicApproximation import logarithmicApproximations
from methods.PowerApproximation import powerApproximations


class Equation:
    def __init__(self, function: Callable, text: str):
        self.function = function
        self.text = text





def toArray(x):
    return np.asarray(x, dtype=float)



def addLinear(coeffs, x):
    return coeffs[0]+coeffs[1]*x

def addQuadratic(coeffs, x):
    return coeffs[0]+coeffs[1]*x+coeffs[2]*x**2
def addCubic(coeffs, x):
    return coeffs[0]+coeffs[1]*x+coeffs[2]*x**2+coeffs[3]*x**3

def addExponential(matrix, x):
    coeffs = exponentialApproximation(matrix)
    return coeffs[0]*math.exp(coeffs[1]*x)

def addLogarithmic(matrix, x):
    coeffs = logarithmicApproximations(matrix)
    # return coeffs[0]*math.log(x)+coeffs[1]
    return coeffs[0]+coeffs[1]*math.log(x)

def addPower(matrix, x):
    coeffs = powerApproximations(matrix)
    return coeffs[0] * (x ** coeffs[1])


def printGraph(ax, canvas, linear, quadratic, cubic, matrix, validX, validY):

    ax.clear()

    # --- исходные точки ---
    x_data = matrix[1]
    y_data = matrix[2]
    ax.scatter(x_data, y_data, color='black', label='Вводные точки')


    min_x = min(x_data)
    max_x = max(x_data)
    delta_x = (max_x - min_x) * 0.25 if max_x != min_x else 1
    x_min = min_x - delta_x
    x_max = max_x + delta_x

    x_vals = np.linspace(x_min, x_max, 1000)

    y_linear    = [addLinear(linear,    x) for x in x_vals]
    y_quadratic = [addQuadratic(quadratic, x) for x in x_vals]
    y_cubic     = [addCubic(cubic,     x) for x in x_vals]
    x_vals_pos = x_vals[x_vals > 0]
    if validX and validY:
        y_pow = [addPower(matrix, x) for x in x_vals_pos]
    if validX:
        y_log = [addLogarithmic(matrix, x) for x in x_vals_pos]
    if validY:
        y_exp = [addExponential(matrix, x) for x in x_vals_pos]



    ax.plot(x_vals, y_linear,    color='blue',   label='Линейная')
    ax.plot(x_vals, y_quadratic, color='orange', label='Квадратичная')
    ax.plot(x_vals, y_cubic,     color='green',  label='Кубическая')
    if validX and validY:
        ax.plot(x_vals_pos, y_pow, color='brown', label='Степенная')
    if validX:
        ax.plot(x_vals_pos, y_log, color='purple', label='Логарифмическая')
    if validY:
        ax.plot(x_vals_pos, y_exp, color='red', label='Экспоненциальная')
    all_y   = y_data + y_linear + y_quadratic + y_cubic
    y_min   = min(all_y)
    y_max   = max(all_y)
    delta_y = (y_max - y_min) * 0.0625 if y_max != y_min else 1
    y_min  -= delta_y
    y_max  += delta_y

    # --- оформление ---
    ax.set_xlim(x_min, x_max)
    ax.set_ylim(y_min, y_max)

    ax.set_title("Аппроксимация данных")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.axhline(0, color='gray', linewidth=1)
    ax.axvline(0, color='gray', linewidth=1)
    ax.grid(True)
    ax.legend()

    canvas.draw()




def clear_graph(ax, canvas):
    ax.clear()
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.grid(True)
    ax.set_title("График уравнения")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    canvas.draw()




