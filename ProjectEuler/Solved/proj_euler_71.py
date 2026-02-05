import math
import time
max_num = 1000000
count = 0

start_time = time.time()
curr_num = 3
curr_den = 8

for x in range(1, max_num):
    min_y = ( 7 * x ) // 3
    max_y = min( ( curr_den * x ) // curr_num, max_num  )
    
    for y in range(min_y, max_y + 1):
        if(x == y or ( x % 2 == 0 and y % 2 == 0) ):
            pass
        else:
            if(math.gcd(x, y) == 1):
                if( ((curr_num * y) <= (curr_den * x) ) and ( (7 * x) < (3 * y) )):
                    curr_num = x
                    curr_den = y
                    count = count + 1
                    # print(curr_num, curr_den, "/", curr_num/curr_den)

print('Final',curr_num, curr_den, "/", curr_num/curr_den)
print(3, 7, '/', 3 / 7)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))