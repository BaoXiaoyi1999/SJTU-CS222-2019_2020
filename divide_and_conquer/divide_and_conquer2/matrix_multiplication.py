import numpy as np


np.random.seed(0)


def matrix_padding(matrix1, matrix2):
    ori_shape1 = matrix1.shape
    ori_shape2 = matrix2.shape
    temp_shape = max(ori_shape1[0], ori_shape1[1], ori_shape2[0], ori_shape2[1])
    if temp_shape == 1:
        return matrix1, matrix2
    scale = 2
    while scale < temp_shape:
        scale = scale * 2
    new_matrix1 = np.zeros(shape=(scale, scale), dtype=int)
    new_matrix2 = np.zeros(shape=(scale, scale), dtype=int)
    new_matrix1[0:ori_shape1[0], 0:ori_shape1[1]] = matrix1
    new_matrix2[0:ori_shape2[0], 0:ori_shape2[1]] = matrix2
    return new_matrix1, new_matrix2


def strassen(n, matrix1, matrix2):
    if n == 1:
        return matrix1 * matrix2
    mid_len = n // 2
    a11 = matrix1[0:mid_len, 0:mid_len]
    a12 = matrix1[0:mid_len, mid_len:]
    a21 = matrix1[mid_len:, 0:mid_len]
    a22 = matrix1[mid_len:, mid_len:]

    b11 = matrix2[0:mid_len, 0:mid_len]
    b12 = matrix2[0:mid_len, mid_len:]
    b21 = matrix2[mid_len:, 0:mid_len]
    b22 = matrix2[mid_len:, mid_len:]

    p1 = strassen(mid_len, a11, (b12 - b22))
    p2 = strassen(mid_len, (a11 + a12), b22)
    p3 = strassen(mid_len, (a21 + a22), b11)
    p4 = strassen(mid_len, a22, (b21 - b11))
    p5 = strassen(mid_len, (a11 + a22), (b11 + b22))
    p6 = strassen(mid_len, (a12 - a22), (b21 + b22))
    p7 = strassen(mid_len, (a11- a21), (b11 + b12))

    c11 = p5 + p4 - p2 + p6
    c12 = p1 + p2
    c21 = p3 + p4
    c22 = p1 + p5 - p3 - p7

    c = np.ndarray(shape=(n, n), dtype=int)
    c[0:mid_len, 0:mid_len] = c11
    c[0:mid_len, mid_len:] = c12
    c[mid_len:, 0:mid_len] = c21
    c[mid_len:, mid_len:] = c22
    return c


ori_matrix1 = np.random.randint(50, size=(15, 15))
ori_matrix2 = np.random.randint(50, size=(15, 15))

print("original matrix1: \n ", ori_matrix1)
print("original matrix2: \n", ori_matrix2)

new_matrix1, new_matrix2 = matrix_padding(ori_matrix1, ori_matrix2)
print("new matrix1: \n", new_matrix1)
print("new matrix2: \n", new_matrix2)

n = new_matrix1.shape[0]
res1 = strassen(n, new_matrix1, new_matrix2)
res2 = np.matmul(new_matrix1, new_matrix2)
print(res1)
print(res2)

