max = 20
len = max+1
wid = max+1
grid = [[0]*len for _ in range(wid)]

for i in range(len):
    grid[i][0] = 1
    grid[0][i] = 1

grid[0][0] = 0

for i in range(1, len):
    for j in range(1, wid):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

print(grid)
print(grid[len-1][wid-1])