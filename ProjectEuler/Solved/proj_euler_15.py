max = 20
length = max+1
wid = max+1
grid = [[0]*length for _ in range(wid)]

for i in range(length):
    grid[i][0] = 1
    grid[0][i] = 1

grid[0][0] = 0

for i in range(1, length):
    for j in range(1, wid):
        grid[i][j] = grid[i-1][j] + grid[i][j-1]

for x in grid:
    print(x)
print(grid[length-1][wid-1])