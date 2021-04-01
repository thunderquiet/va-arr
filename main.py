

def consecutive_sum(n, m, array):
	min_sum = 0
	sum = 0
	for q in range(0, n):
		sum += array[q]
	min_sum = sum

	for i in range(n, m):
		sum -= array[i-n]
		sum += array[i]
		if( sum < min_sum ):
			min_sum = sum
	return min_sum


if __name__ == "__main__":
	min_sum = consecutive_sum2( 4, 5, [5,6,2,1,9] )
	print( min_sum )

