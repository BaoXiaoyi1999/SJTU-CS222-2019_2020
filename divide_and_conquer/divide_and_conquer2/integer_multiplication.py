import random
from math import ceil

random.seed(0)


def bit_multiplication(bit_string1, bit_string2, n):
    if n == 1:
        if not bit_string1 or not bit_string2:
            return 0
        return int(bit_string1) * int(bit_string2)
    else:
        m = n // 2   # exists k, such that m = 2 ** k
        string1_1 = bit_string1[0:m]
        string1_2 = bit_string1[m:]
        string2_1 = bit_string2[0:m]
        string2_2 = bit_string2[m:]
        e = bit_multiplication(string1_1, string2_1, m)
        f = bit_multiplication(string1_2, string2_2, m)
        g = bit_multiplication(string1_2, string2_1, m)
        h = bit_multiplication(string1_1, string2_2, m)
        return 2 ** (2 * m) * e + 2 ** m * (g + h) + f


num1 = random.choice(range(100))
num2 = random.choice(range(100))
bit_string1 = bin(num1)[2:]
bit_string2 = bin(num2)[2:]

print("original string1:", bit_string1)
print("original string2:", bit_string2)
if len(bit_string1) < len(bit_string2):
    bit_string1 = "0" * (len(bit_string2) - len(bit_string1)) + bit_string1
    len_of_bit = len(bit_string2)
elif len(bit_string1) > len(bit_string2):
    bit_string2 = "0" * (len(bit_string1) - len(bit_string2)) + bit_string2
    len_of_bit = len(bit_string1)
else:
    len_of_bit = len(bit_string1)

scale = 2
while scale < len_of_bit:
    scale = scale * 2
bit_string1 = "0" * (scale - len_of_bit) + bit_string1
bit_string2 = "0" * (scale - len_of_bit) + bit_string2
len_of_bit = scale

print("bitstring1: ", bit_string1)
print("bitstring2: ", bit_string2)

res = bit_multiplication(bit_string1, bit_string2, len_of_bit)
print("num1=", num1)
print("num2=", num2)
print(num1 * num2)
print(res)
