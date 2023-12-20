out = 0
for base in range(1,10):
    power = 1
    while(True):
        num = base ** power
        num_d = len(str(num))
        if(num_d == power):
            out += 1
            print(num_d, power, num)
        elif(num_d < power):
            power = 1
            break
        power = power+1
print(out)