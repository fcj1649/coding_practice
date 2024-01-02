import sys
# adding  to the system path
sys.path.insert(0, '.\Common')
import mathOp
import time
start_time = time.time()
power = 7830457
mod = 10 ** 10
num = 28433
for j in range(power):
    num = num * 2 % mod
num = ( num + 1 )

print(num)

endtime = time.time()
print("--- %s seconds ---" % (endtime-start_time))