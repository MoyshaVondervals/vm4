def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    det = 0
    for col in range(n):
        elem = matrix[0][col]

        # формируем минор
        minor = []
        for r in range(1, n):
            row_minor = []
            for c in range(n):
                if c == col:
                    continue
                row_minor.append(matrix[r][c])
            minor.append(row_minor)

        sign = -1 if col % 2 else 1
        det += sign * elem * determinant(minor)

    return det


def findCoeffs(matrix, vector):
    size  = len(matrix)
    det_A = determinant(matrix)
    if det_A == 0:
        raise ValueError("Система не имеет единственного решения (det(A) = 0).")

    coeffs = []
    for col in range(size):
        Ai = []
        for r in range(size):
            row_copy = []
            for c in range(size):
                row_copy.append(matrix[r][c])
            Ai.append(row_copy)
        for r in range(size):
            Ai[r][col] = vector[r]
        det_Ai = determinant(Ai)
        coeffs.append(round(det_Ai / det_A, 6))
    return coeffs
