from decimal import *
from mpmath import *
import time

from spoj_chg_270_pival import piDig

def main():
    start_time = time.time()
    act = [x for x in str(piDig(3000001, 100))]
    end_time = time.time()
    mp.dps=100
    exp = [x for x in str(mp.pi)]
    print("".join(act))
    print("".join(exp))
    for i in range(0 , 100):
        if(i < len(act) and i < len(exp)):
            if(act[i] != exp[i]):
                print(i+1)
                break
    print("--- %s seconds ---" % (end_time - start_time))

if __name__ == "__main__":
    main()
