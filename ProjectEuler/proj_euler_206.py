import math

for i in range(0,10):
    sqr = ''
    for j in range(1,11):
        sqr += str(j%10) + str(i)
    root = math.sqrt(int(sqr))
    if(root.is_integer()):
        print(root, sqr)