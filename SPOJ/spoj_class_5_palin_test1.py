import math
start = 100
end = 100000

def copy_num(num : list, left : int, right: int):
    while( left >= 0 and right < len(num)):
        num[right] = num[left]
        left = left - 1
        right = right + 1
    return num

for i in range(start, end):
    data = [int(i) for i in str(i)]
    left = 0
    right = 0 
    mid = int(math.floor(len(data) / 2))
    if(len(data) % 2 == 0):
        left = mid - 1
        right = mid
    else:
        left = mid - 1
        right = mid + 1

    data = copy_num(data, left, right)    
    data_str = "".join((str(x) for x in data))
    new_num = int(data_str)

    print(str(i) + "," + data_str + "," + str( new_num > i ))