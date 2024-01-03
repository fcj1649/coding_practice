prime = [2, 3, 5, 7, 11, 13, 17, 19, 23]

prod = 1        
for idx, num in enumerate(prime):
    prod *= num

print(prod)