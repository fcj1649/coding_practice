import math
import pathlib, os
path = os.path.join(pathlib.Path(__file__).parent.resolve(),'proj_euler_8_input.txt')

num = ''
file = open(path, 'r')
for line in file.readlines():
    num = num + line.strip()

seq = 13
max_prod = -1
for i in range(len(num)-seq+1):
    prod = math.prod(int(x) for x in num[i:i+seq])
    if prod > max_prod:
        max_prod = prod
print(max_prod)