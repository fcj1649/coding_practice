import math
def checkPentagonal(num: int):
    a = 3
    b = -1
    c = -2 * num
    # only first part is needed
    if((b * b - 4 * a * c) >= 0):
        root_1 = (-b + math.sqrt(b * b - 4 * a * c)) / ( 2 * a )
        if(root_1.is_integer() and root_1 > 0):
            return True
        else: 
            return False
    return False

def checkHexagonal(num: int):
    a = 2
    b = -1
    c = -1 * num
    # only first part is needed
    if((b * b - 4 * a * c) >= 0):
        root_1 = (-b + math.sqrt(b * b - 4 * a * c)) / ( 2 * a )
        if(root_1.is_integer() and root_1 > 0):
            return True
        else: 
            return False
    return False

def getTriangleNo(n:int):
    return int(n * (n+1) / 2)

n = 285
while(True):
    n+=1
    tri = getTriangleNo(n)
    if(checkPentagonal(tri) and checkHexagonal(tri)):
        print(tri)
        break