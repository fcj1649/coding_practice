import random
import mathOp
test_cases = 10
max = 100000000
for i in range(test_cases):
    num1 = random.randint(1, max)
    num2 = random.randint(1, max)
    prod_exp = str(num1*num2)
    prod_act = "".join(str(x) for x in mathOp.prodInt([int(x) for x in str(num1)], [int(x) for x in str(num2)]))
    print(num1, num2, prod_exp, prod_act, prod_act == prod_exp)