import math
from audioop import error
from collections.abc import Callable

import numpy as np


class Equation:
    def __init__(self, function: Callable, text: str):
        self.function = function
        self.text = text




predefined_functions = {
    1: Equation(lambda x: ((18*x)/(x**4+10)), r"18x/(x^4+10)"), #2x-1
    2: Equation(lambda x: (0.4*x**2-3*x+5), r"0.4x^2 - 3x + 5"),
    3: Equation(lambda x: (-0.2*x**3+1.5*x**2-4*x+2), r"-0.2x^3 + 1.5x^2 - 4x + 2"),
    4: Equation(lambda x: (math.e**(0.7*x)), r"3e^{0.7x}"),
    5:Equation(lambda x: (2*math.log(x)-1), r"2*ln(x) - 1"),
    6:Equation(lambda x: (5*x**(0.8)), r"5x^{0.8}"),
}







def addLinear(coeffs, x):
    return coeffs[0]+coeffs[1]*x

def addQuadratic(coeffs, x):
    return coeffs[0]+coeffs[1]*x+coeffs[2]*x**2
def addCubic(coeffs, x):
    return coeffs[0]+coeffs[1]*x+coeffs[2]*x**2+coeffs[3]*x**3

def addExponential(coeffs, x):
    return coeffs[0]*math.exp(coeffs[1]*x)

def addLogarithmic(coeffs, x):
    return coeffs[0]+coeffs[1]* math.log(x)

def addPower(coeffs, x):
    return coeffs[0]*(x**coeffs[1])

def printGraph(ax, canvas, a, b, linear, quadratic, cubic, matrix, limitation):

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
    if not limitation:

        y_exp = [addExponential(linear, x) for x in x_vals_pos]
        y_log = [addLogarithmic(linear, x) for x in x_vals_pos]
        y_pow = [addPower(linear, x) for x in x_vals_pos]



    ax.plot(x_vals, y_linear,    color='blue',   label='Линейная')
    ax.plot(x_vals, y_quadratic, color='orange', label='Квадратичная')
    ax.plot(x_vals, y_cubic,     color='green',  label='Кубическая')
    if not limitation:
        ax.plot(x_vals_pos, y_exp, color='red', label='Экспоненциальная')
        ax.plot(x_vals_pos, y_log, color='purple', label='Логарифмическая')
        ax.plot(x_vals_pos, y_pow, color='brown', label='Степенная')

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


def checkBrakePoints(eq_num, left_bound, right_bound):
    f = predefined_functions[eq_num].function

    try:
        val = f(left_bound)
        if isinstance(val, complex):
            return []
    except (ZeroDivisionError, OverflowError, ValueError):
        return []

    try:
        val = f(right_bound)
        if isinstance(val, complex):
            return []
    except (ZeroDivisionError, OverflowError, ValueError):
        return []

    width = right_bound - left_bound
    n = math.ceil(width * 1000)
    if n < 1:
        n = 1

    h = width / n

    valid_intervals = []
    in_valid_segment = False
    current_start = None

    def can_evaluate(x):
        try:
            val = f(x)
            if isinstance(val, complex):
                return False
            return True
        except (ZeroDivisionError, OverflowError, ValueError):
            return False

    for i in range(n + 1):
        point = left_bound + i * h
        if i == n:
            point = right_bound

        if can_evaluate(point):
            if not in_valid_segment:
                in_valid_segment = True
                current_start = point
        else:
            if in_valid_segment:
                in_valid_segment = False

                valid_intervals.append((round(current_start, 6), round(point - h, 6)))

    if in_valid_segment:
        valid_intervals.append((round(current_start, 6), round(right_bound, 6)))



    return valid_intervals






