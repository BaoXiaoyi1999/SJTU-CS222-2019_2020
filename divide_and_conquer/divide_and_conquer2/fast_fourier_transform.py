import cmath


def fft(n, arr):
    # where arr is the array which contains the coefficient of a polynomial.
    # assert there exists k, such that 2 ** k = n
    n = len(arr)
    if arr == 1:
        return arr[0]
    even_coefficients = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    odd_coefficients = [arr[i] for i in range(len(arr)) if i % 2 != 0]
    print(even_coefficients)
    print(odd_coefficients)
    sub_array1 = fft(n/2, even_coefficients)
    sub_array2 = fft(n/2, odd_coefficients)

    res_array1 = []
    res_array2 = []
    for k in range(int(n//2)):
        w_k = cmath.exp(complex(0, (2 * cmath.pi * k)/n))
        y_k = sub_array1[k] + w_k * sub_array2[k]
        y_kplushalfn = sub_array1[k] - w_k * sub_array2[k]
        res_array1.append(y_k)
        res_array2.append(y_kplushalfn)
    res = res_array1 + res_array2
    return res


def inverse_fft(n, arr):
    if n == 1:
        return arr[0]
    even_coefficients = [arr[i] for i in range(len(arr)) if i % 2 == 0]
    odd_coefficients = [arr[i] for i in range(len(arr)) if i % 2 != 0]
    print(even_coefficients)
    print(odd_coefficients)
    sub_array1 = fft(n/2, even_coefficients)
    sub_array2 = fft(n/2, odd_coefficients)

    res_array1 = []
    res_array2 = []
    for k in range(int(n//2)):
        w_k = cmath.exp(complex(0, (- 2 * cmath.pi * k)/n))
        y_k = sub_array1[k] + w_k * sub_array2[k]
        y_kplushalfn = sub_array1[k] - w_k * sub_array2[k]
        res_array1.append(y_k)
        res_array2.append(y_kplushalfn)
    res = res_array1 + res_array2
    return res
