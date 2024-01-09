f1 = 1 
f2 = 2
f3 = 3
fib_sum = 2
while( f3 <= 4 * 10 ** 6):
    f1 = f2
    f2 = f3
    f3 = f1 + f2

    if( f3 % 2 == 0):
        fib_sum = fib_sum + f3

print(fib_sum)