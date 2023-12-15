import time
def makePalin(input: str, isOdd: bool):
    mid = int(len(input) / 2)
    res = input[0:mid+1]
    if(isOdd):
        j = mid - 1
    else:
        j = mid
    
    while(j>=0):
        res += input[j]
        j-=1
    return res
    

def checkPalin(input: str):
    i = 0
    j = len(input) - 1
    isPalin = True
    while(i<=j):
        if(input[i] != input[j]):
            isPalin = False
            break
        i += 1
        j -= 1

    return isPalin

max = 1000000
start_time = time.time()
sum = 0
for i in range(1, max):
    if(checkPalin(str(i))):
        bi = bin(i).replace("0b", "") 
        if(checkPalin(bi)):
            sum += i
            print(i, bi)
print(sum)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))

start_time = time.time()
sum = 0
palinList = {}
i = 1
num = 1
while(num <= max):
    numStr = makePalin(str(i), True)
    num = int(numStr)
    bi = bin(num).replace("0b", "") 
    if(checkPalin(bi) and not num in palinList):
        sum += num
        palinList[num] = True
        print(num, bi)
    i += 1

i = 1
num = 1
while(num <= max):
    numStr = makePalin(str(i), False)
    num = int(numStr)
    bi = bin(num).replace("0b", "") 
    if(checkPalin(bi) and not num in palinList):
        sum += num
        palinList[num] = True
        print(num, bi)
    i += 1

print(sum)
end_time = time.time()
print("--- %s seconds ---" % (end_time - start_time))