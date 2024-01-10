
def pythTriple(n: int):
    for a in range(1, int(n / 3)):
        for b in range(a, int(n / 2)):
            c = n - a - b
            if( c*c == a*a + b*b ):
                print(a*b*c, a, b, c, c*c, a*a, b*b)

pythTriple(3000)