import math

def rev(num):
	return int(num != 0) and ((num % 10) * \
			(10**int(math.log(num, 10))) + \
						rev(num // 10))

test_number = 9288811

new_number = test_number
res = False 

while(not res):
    new_number = new_number + 1
    res = new_number == rev(new_number)

print (str( test_number ) + " Next palindrome:" + str(new_number))
