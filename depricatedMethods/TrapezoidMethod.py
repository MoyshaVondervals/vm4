from utils.Utils import predefined_functions

def runge(I, I_previous, k):
    return (I_previous - I)/(2**k - 1)

def trapezoid_solution(eq_num, a, b, epsilon):
    n = 4
    matrix = []


    f = predefined_functions[eq_num].function

    max_iterations = 1000
    I_previous = 1000
    iterations = 0
    while True:
        if iterations > max_iterations:
            return 1, [], 0
        h = (b - a) / n
        x_values = [a + h * i for i in range(n)]
        f_values = [f(i) for i in x_values]

        I = h/2 * (f_values[0] + f_values[-1] + 2 * (sum(y for y in f_values) - f_values[0] + f_values[-1]))
        row = [iterations, n, round(I, 6), round(I_previous, 6)]
        matrix.append(row)
        if (abs(runge(I, I_previous, 2)) < epsilon):
            break
        I_previous = I
        n *= 2
        iterations += 1
    return 0, matrix, I
