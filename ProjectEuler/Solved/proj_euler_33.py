import math
out_num = 1
out_den = 1
for num in range(10,100):
    for den in range(num+1,100):
        num_1 = int(num/10)
        num_2 = num % 10
        den_1 = int(den/10)
        den_2 = den % 10
        if(num == 49 and den == 98):
            pass
        if(num_2 == den_1 and den_2 != 0):
            actual = num / den
            calc   = num_1 / den_2
            if(actual == calc):
                print(num, den)
                out_num *= num
                out_den *= den
print(out_num, out_den)
gcd = math.gcd(out_num, out_den)
out_num = out_num / gcd
out_den = out_den / gcd
print(out_num, out_den)