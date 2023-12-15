import sys
# adding  to the system path
sys.path.insert(0, '.\Common')
import mathOp
import random

print(sum(map(int,str(2 ** 1000))))

prod = [1]

for i in range(1, 1001):
    prod = mathOp.prodInt(prod, [2])

print(sum(x for x in prod))