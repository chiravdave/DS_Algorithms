"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers can be 0 or negative.
"""

def largest_sum(a: list) -> int:
	"""
	This function will return largest sum of non-adjacent numbers.

	:param a: input list of numbers
	:rtype: largest sum of non-adjacent numbers
	"""

	# To store the maximum sum before the previous element
	prev_prev_sum = 0
	# To store the maximum sum before the current element
	prev_sum = 0
	# To check if the array contains only negative no.s
	flag = True
	# Looping through every number
	for no in a:
		temp = prev_sum
		# Calculating prev_sum for the next element
		prev_sum = max(prev_sum, prev_prev_sum+no)
		# Calculating prev_prev_sum for the next element
		prev_prev_sum = max(temp, prev_prev_sum)
		# Checking if we have any non-negative no
		if no >= 0:
			flag = False

	if flag:
		return max(a)

	return max(prev_prev_sum, prev_sum)

if __name__ == "__main__":
	print(largest_sum([2, 8, 5]))