import math
matrix = [[]]
file = open('.\ProjectEuler\proj_euler_81.txt', 'r')
for line in file.readlines():
    matrix.append([int(x) for x in line.strip().split(',')])

matrix.pop(0)
#print(matrix)
size = len(matrix)
# top column and first row
for i in range(1, size):
    matrix[i][0] = matrix[i-1][0] + matrix[i][0] 
    matrix[0][i] = matrix[0][i-1] + matrix[0][i]

for i in range(1,size):
    for j in range(1,size):
        matrix[i][j] = matrix[i][j] + min(matrix[i-1][j],matrix[i][j-1])

print(matrix[size-1][size-1])