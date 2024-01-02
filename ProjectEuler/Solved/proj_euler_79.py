import math
import pathlib, os
path = os.path.join(pathlib.Path(__file__).parent.resolve(),'proj_euler_0079_keylog.txt')

file = open(path, 'r')
left = {}
right = {}

for i in range(0,10):
    left[i] = []
    right[i] = []

for line in file.readlines():
    num_arr =[int(x) for x in line.strip()]
    for i in range(len(num_arr)):
        temp_left = num_arr[0:i]
        left[num_arr[i]].extend(temp_left)
        temp_right = num_arr[i+1:len(num_arr)-i]
        right[num_arr[i]].extend(temp_right)

for i in range(0,10):
    print(i, set(left[i]), set(right[i]))
