n = 100

sum_of_sq = int((n * (n+1) * (2 * n+1)) / 6)
sum = int(n * (n+1) / 2)
sq_of_sum = sum * sum

print(sq_of_sum - sum_of_sq)