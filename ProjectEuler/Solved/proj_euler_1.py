def get_sum_mul(num: int, mul: int):
    num = num // mul
    return mul * num * (num+1) // 2

num = 1000 - 1
print(get_sum_mul(num, 3) + get_sum_mul(num, 5) - get_sum_mul(num, 15))        