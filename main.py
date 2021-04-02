

def consecutive_sum(n, m, array):
	# data type checks since python is not statically-typed
	if( not isinstance(n, int) or not isinstance(m, int) or not isinstance(array, list) ):
		raise TypeError("Wrong input type. N and M must be integers. Array must be a python list.")

	# range checks
	if( n > m or m != len(array) or n < 0 or m < 0 ):
		raise RuntimeError("Invalid input range. N must be less than M. M must match Array length. N and M must be positive.")

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
	min_sum = consecutive_sum( 3, 5, [5,6,2,1,9] )
	print( min_sum )

