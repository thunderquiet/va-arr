


def consecutive_sum(n, m, array):
	min_sum = 0
	c = 0
	for i in range(0, m-n):
		c+=1
		sum = 0
		for q in range(0, n):
			c+=1
			sum += array[i+q]
		if( min_sum == 0 or sum < min_sum ):
			min_sum = sum
	print( c )
	return min_sum


def consecutive_sum2(n, m, array):
	min_sum = 0
	c = 0
	sum = 0
	for q in range(0, n):
		c+=1
		sum += array[q]
	min_sum = sum

	for i in range(n, m):
		c+=1
		sum -= array[i-n]
		sum += array[i]
		if( sum < min_sum ):
			min_sum = sum
	
	print( c )
	return min_sum


if __name__ == "__main__":
	min_sum = consecutive_sum2( 4, 5, [5,6,2,1,9] )
	print( min_sum )


# (n+1)*(m-n) = n*(m-n)

# 2  3  4
# 9, 8, 5


# 5(3), 5(9) 5(14)
# m

# best version can't be run in parallel -> double for-loop can be in paralle map-reduce style
