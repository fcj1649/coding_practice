file = open('.\ProjectEuler\Solved\proj_euler_0067_triangle.txt', 'r')
grid = [[]]
for line in file.readlines():
    nums = [int(x) for x in line.strip().split(" ")]
    grid.append(nums)
grid.pop(0)

i = len(grid) - 2
while(i>=0):
    for j in range(len(grid[i])):
        grid[i][j] = grid[i][j] + max(grid[i+1][j],grid[i+1][j+1])    
    i-=1
print(grid)
print(grid[0][0])