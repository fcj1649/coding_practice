import math
import spoj_class_5_palin

def rev(num):
	return int(num != 0) and ((num % 10) * \
			(10**int(math.log(num, 10))) + \
						rev(num // 10))

try:
	test_case = int(input())
except EOFError:
	test_case = 0

for i in range(test_case):
	test_number = int(input())
	new_number = test_number
	res = False 

	while(not res):
		new_number = new_number + 1
		res = new_number == rev(new_number)

	act_res = spoj_class_5_palin.next_palin(str(test_number))
	final_res = act_res == str(new_number) 
	print (str(final_res) + " Inp:" + str(test_number) + " Exp:" + str(new_number) + " Act:" + act_res)