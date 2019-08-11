def maxSubArray(A):
	    best = -inf
	    sumsofar = 0
	    for x in A:
	        sumsofar += x
	        best = max(sumsofar, best)
	        # Doing this last, to handle case
	        # when all numbers are negative.
	        sumsofar = max(sumsofar, 0)
	    return best

A = [1,-2,-3,4,-4,-9]
maxSubArray(A)
