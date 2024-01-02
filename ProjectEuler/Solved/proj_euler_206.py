import math
import time
start_time = time.time()
checkArr = ['1','','2','','3','','4','','5','','6','','7','','8','','9','','0','',]

for i in range(10**9, 10**10, 10):
    res = str(i ** 2)
    if(len(res)>19):
        break
    elif(len(res) == 19):
        isValid = True
        for k in range(0,len(res),2):
            if(res[k] != checkArr[k]):
                isValid = False
                break
        if(isValid):
            print("Result:",i, res)
            break
end_time = time.time()
print('--- %s seconds ---' % (end_time-start_time))