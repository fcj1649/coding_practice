import math

def fraction_sum(frac1:tuple, frac2:tuple):
    den = frac1[1] * frac2[1]
    num = (frac1[1] * frac2[0]) + (frac1[0] * frac2[1])
    return num, den

def reverse_frac(frac:tuple):
    return frac[1],frac[0]

max = 100

seq =[1]
n = 2
while(len(seq)<=max):
    seq.append(n)
    seq.append(1)
    seq.append(1)
    n+=2

k = max
curr = (seq[k-2],1)
for j in reversed(range(k-2)):
    first = (seq[j],1)
    second = reverse_frac(curr)
    curr = fraction_sum(first, second)
curr = fraction_sum((2,1),reverse_frac(curr))
print(curr)
print(sum(int(x) for x in str(curr[0])))