x = 2
while(True):
    dig_set = set(list(str(x)))
    found = True
    for i in range(2,7):
        new_set = set(list(str(i * x)))
        if(new_set != dig_set):
            found = False
            break
    if(found):
        break
    else:
        x+=1
print(x)

for j in range(1,7):
    print(j*x)