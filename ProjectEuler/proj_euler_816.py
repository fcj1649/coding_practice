import decimal
def distance(x: tuple, y:tuple):
    x_dis = decimal.Decimal(x[0] - y[0]) * decimal.Decimal(x[0] - y[0])
    y_dis = decimal.Decimal(x[1] - y[1]) * decimal.Decimal(x[1] - y[1])
    dis = x_dis + y_dis
    return dis.sqrt()

s0 = 290797
mod_val = 50515093


k = 2000000

points = [0] * k
s_arr = [0] * (2 * k + 1)

s_arr[0] = s0

for i in range(1, 2*k+1):
    s_arr[i] = (( s_arr[i-1] % mod_val ) * ( s_arr[i-1] % mod_val )) % mod_val

for i in range(0, k):
    points[i] = (s_arr[2*i], s_arr[2*i+1])

min_dis = distance(points[0], points[1])

for i in range(k):
    for j in range(i+1, k):
        dis = distance(points[i], points[j])
        if(dis < min_dis):
            min_dis = dis

print(round(min_dis,9))