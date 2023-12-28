def coin_sum(coins:list, total:int):
    grid = [[0 for x in range(total+1)] for y in range(len(coins))]
    
    for row in grid:
        row[0] = 1

    for i in range(len(grid)):
        for j in range(1, len(grid[i])):
            if(j - coins[i] >= 0):
                # remove the coin from total sum
                grid[i][j] = grid[i-1][j] + grid[i][j-coins[i]]
            else:
                # this is without the current coin
                grid[i][j] = grid[i-1][j]        
    
    for row in grid:
        print(row)                        
    
    return grid[len(coins)-1][total]


print(coin_sum([1,2,5,10,20,50,100,200], 200))

