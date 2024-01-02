import math
import pathlib, os
from decimal import Decimal
path = os.path.join(pathlib.Path(__file__).parent.resolve(),'proj_euler_0099_base_exp.txt')

str = ''
file = open(path, 'r')
max_res = Decimal(0)
line_no = 0
max_line = 0
for line in file.readlines():
    line_no +=1
    num_arr = [int(x) for x in line.strip().split(',')]
    base = Decimal(num_arr[0])
    expo = Decimal(num_arr[1])
    res = expo * Decimal.log10(base)
    if(res > max_res):
        max_res = res
        max_line = line_no
print(max_line)

