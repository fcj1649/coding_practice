
def pythTriple(n: int):
    for a in range(1, int(n / 3)):
        for b in range(a, int(n / 2)):
            c = n - a - b
            if( c*c == a*a + b*b ):
                print(a*b*c, a, b, c, c*c, a*a, b*b)

pythTriple(3000)

import math
max_N = 3000 + 1
out = [-1] * max_N

for a in range(1, max_N):
    for b in range(a, max_N - a):
        c_sqr = a * a + b * b
        c = math.sqrt(c_sqr)
        if (c.is_integer()):
            if(a+b+c < max_N):
                if a*b*c > out[a+b+int(c)]:
                    out[a+b+int(c)] = a*b*c
print(out[3000])