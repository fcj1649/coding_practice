import math
str = ''
file = open('.\ProjectEuler\Solved\proj_euler_8_input.txt', 'r')
for line in file.readlines():
    str = str + line.strip()

seq = 13
max = -1
for i in range(len(str)-seq+1):
    prod = math.prod(int(x) for x in str[i:i+seq])
    if(prod > max):
        max = prod

print(max)