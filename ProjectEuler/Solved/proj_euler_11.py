file = open('.\ProjectEuler\Solved\proj_euler_11.txt', 'r')
grid = [[]]
for line in file.readlines():
    nums = [int(x) for x in line.strip().split(" ")]
    grid.append(nums)
grid.pop(0)
print(grid)

prod = -1

for i in range(0, len(grid)):
    for j in range(3, len(grid[i])):
        prod = max(prod, grid[i][j] * grid[i][j-1] * grid[i][j-2] * grid[i][j-3])

for i in range(0, len(grid)):
    for j in range(3, len(grid[i])):
        prod = max(prod, grid[i][j] * grid[i][j-1] * grid[i][j-2] * grid[i][j-3])

for i in range(3, len(grid)):
    for j in range(3, len(grid[i])):
        prod = max(prod, grid[i][j] * grid[i-1][j-1] * grid[i-2][j-2] * grid[i-3][j-3])                

for i in range(0, len(grid) - 3):
    for j in range(3, len(grid[i])):
        prod = max(prod, grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3])   

print(prod)