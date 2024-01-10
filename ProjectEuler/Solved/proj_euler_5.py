max = 20

def checkOne(num: list):
    valid = True
    for i in range(1, len(num)):
        if(num[i]!=1):
            valid = False
            break
    return valid

list_num = [True] * max

list_num[0] = False
list_num[1] = False

for i in range(2, max):
    if(list_num[i]):
        j = i * 2
        while( j < max):
            list_num[j] = False
            j = j + i

list = [0] * (max + 1)

for i in range(len(list)):
    list[i] = i

out = []

while(not checkOne(list)):
    for idx, num in enumerate(list_num):
        if(num): 
            #prime
            isDiv = False
            for i in range(1 , len(list)):
                if(list[i] % idx == 0):
                    list[i] = int(list[i] / idx)
                    isDiv = True
            if(isDiv):
                out.append(idx)
prod = 1
for x in out:
    prod *= x
print(out)
print(prod)

