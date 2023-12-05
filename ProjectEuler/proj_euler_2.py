f1 = 1 
f2 = 2
f3 = 3
sum = 2
while( f3 <= 4000000):
    f1 = f2
    f2 = f3
    f3 = f1 + f2

    if( f3 % 2 == 0):
        sum = sum + f3

print(sum)