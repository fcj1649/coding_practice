import math
def rev(num):
	return int(num != 0) and ((num % 10) * \
			(10**int(math.log(num, 10))) + \
						rev(num // 10))

def main():
	out = []
	for i in reversed(range(1000)):
		j = 999
		while( j >= i):
			if( i*j == rev(i*j)):
				out.append(i*j)
			j -= 1
	out.sort(reverse=True)
	print(out[0])


if __name__ == "__main__":
    main()