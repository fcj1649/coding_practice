max_sum = -1

for a in range(2,100):
    for b in range(2,100):
        num = a**b
        dig_sum = sum(int(x) for x in str(num))
        if(dig_sum > max_sum):
            max_sum = dig_sum
            out = (a,b)

print(max_sum, out)