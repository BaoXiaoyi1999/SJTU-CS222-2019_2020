
def complex_multiplication(a_r, a_i, b_r, b_i):
    ac = a_r * b_r
    bd = a_i * b_i
    sum_ab_mul_sum_cd = (a_r + a_i) * (b_r + b_i)
    res_r = ac - bd
    res_i = sum_ab_mul_sum_cd - ac - bd
    return res_r, res_i
