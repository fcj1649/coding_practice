#pan dig products
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
        if(len(pan) == 9 and ('0' not in pan)):
            dig = set(list(pan))
            if(len(dig) == 9):
                print(pan, a, b, c)
                out.append(c)
out.sort()
print(out)
out = list(set(out))
print(sum(x for x in out))

