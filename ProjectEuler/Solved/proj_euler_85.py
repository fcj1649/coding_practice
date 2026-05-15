import numpy as np
import math

num = 2000000
coeffs = [1, 1, -1 * num * 2]
roots = np.roots(coeffs)

print(roots)

max_iter = int(math.ceil((max(roots[0], roots[1]))))
print(max_iter)

diff = num
out = []
final_rect = 0


for i in range(1, max_iter):
    for j in range(1, max_iter):
        rectangle_count = (i * (i+1)) * (j * (j+1)) / 4
        if( abs(num - rectangle_count) <= diff ):
            diff = abs(num - rectangle_count)
            out = [i, j]
            final_rect = rectangle_count

print(out,out[0] * out[1],diff,final_rect)