from decimal import *
def piDig(iteration:int, precision:int):
    getcontext().prec = precision
    pi = Decimal(4)
    sign = 4
    odd = 1
    num = iteration
    for i in range(1, num):
        odd = 2 * i + 1
        sign = sign * -1
        pi = pi + Decimal( sign ) / Decimal( odd )

    #madhava corr
    pi = pi - Decimal ( 4 ) * Decimal( num * num + 1) / Decimal( 4 * num * num * num + 5 * num)
    return pi

def main():
    print(piDig(10000001, 100))

if __name__ == "__main__":
    main()
