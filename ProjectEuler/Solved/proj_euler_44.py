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

max_pen = 5000    
for j in range(1, max_pen):
    p_j = int(j * (3 * j - 1) / 2)
    for k in range(j+1, max_pen):
        p_k = int(k * (3 * k - 1) / 2)

        if(checkPentagonal(p_k-p_j) and checkPentagonal(p_k+p_j)):
            print(p_k, p_j, k, j, p_k-p_j)