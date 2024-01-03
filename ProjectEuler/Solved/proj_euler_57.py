import math

def fraction_sum(frac1:tuple, frac2:tuple):
    den = frac1[1] * frac2[1]
    num = (frac1[1] * frac2[0]) + (frac1[0] * frac2[1])
    return num, den

def reverse_frac(frac:tuple):
    return frac[1],frac[0]


def reduce_frac(frac:tuple):
    gcd = math.gcd(frac[0], frac[1])
    if(gcd > 1):
        return int(frac[0]/gcd), int(frac[1]/gcd)
    else:
        return frac
    
max = 1000

terms = {0:(0,0), 1:(1,2)}
for i in range(2, max+1):
    terms[i] = reverse_frac(fraction_sum((2,1),terms[i-1]))

for i in range(max+1):
    terms[i] = fraction_sum((1,1),terms[i])
count = 0
for i in range(max+1):
    if(len(str(terms[i][0])) > len(str(terms[i][1]))):
        print(i, terms[i])
        count += 1
print(count)