import math

def getK(p: int, n: int, s: int):
    return int(math.floor((p-n)/s))

def getPossibleSum(n:int, s:int):
    out = []
    for i in range(1*n, s*n +1):
        out.append(i)
    return out
number = 6
sides = 6
[print(x,getK(x,number,sides)) for x in getPossibleSum(number,sides)]