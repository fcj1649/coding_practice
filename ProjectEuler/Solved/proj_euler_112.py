max_num = 10000000
bouncy = 0
tot = 99
for x in range(100, max_num):
    dig_list = [int(digit) for digit in str(x)]
    inc = True
    dec = True
    tot = tot + 1
    for i in range(1, len(dig_list)):
        if(dig_list[i]<dig_list[i-1]):
            dec = False
        if(dig_list[i]>dig_list[i-1]):
            inc = False
        if(not(inc or dec)):
            bouncy = bouncy + 1
            break
    if(0.99 == bouncy / tot):
        break

print("bouncy", bouncy)
print("total", tot)
print(bouncy/tot)    
