import math
start = 100
end = 100000

def rev(num):
	return int(num != 0) and ((num % 10) * \
			(10**int(math.log(num, 10))) + \
						rev(num // 10))

for i in range(start, end):
    if(i == rev(i)):
        print(i)