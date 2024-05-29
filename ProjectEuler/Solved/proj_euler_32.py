#pan dig products
def pandigital(inp:int):
    chk = ''
    for i in range(inp):
        chk += str(i+1)
    out = []
    for a in range(1, 10000):
        dig_a = len(str(a))
        dig_b = 5 - dig_a - 1
        min_b = 10 ** dig_b
        max_b = 10 ** (dig_b+1) - 1
        if(a == 39):
            pass
        for b in range(min_b, max_b+1):
            c = a * b
            pan = str(a) + str(b) + str(c)
            
            if(len(pan) == inp and ('0' not in pan)):
                dig = set(list(pan))
                if(len(dig) == inp):
                    print(pan, a, b, c)
                    out.append(c)
    out.sort()
    print(out)
    out = list(set(out))
    return out



for i in range(4,10):
    print(sum(x for x in pandigital(i)))
