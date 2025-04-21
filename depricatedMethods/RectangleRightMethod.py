from utils.Utils import predefined_functions

def runge(I, I_previous, k):
    return (I_previous - I)/(2**k-1)

def right_rectangles_solution(eq_num, a, b, epsilon):
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
        x_values = [a + h + h * i for i in range(n)]
        f_values = [f(i) for i in x_values]
        I = sum(y * h for y in f_values)
        row = [iterations, n, round(I, 6), round(I_previous, 6)]
        matrix.append(row)
        if abs(runge(I, I_previous, 2)) < epsilon and I_previous - I !=0:
            break
        n *= 2
        iterations += 1
        I_previous = I

    return 0, matrix, I