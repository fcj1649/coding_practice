import math

def fraction_sum(frac1:tuple, frac2:tuple):
    den = frac1[1] * frac2[1]
    num = (frac1[1] * frac2[0]) + (frac1[0] * frac2[1])
    return num, den

def reverse_frac(frac:tuple):
    return frac[1],frac[0]

max = 10

count = 0

for i in range(1,max+1):
    for j in range(i):
        pass