"""
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers.
Numbers are only positive.
"""

def largest_sum(a: list) -> int:
	"""
	This function will return largest sum of non-adjacent numbers.

	:param a: input list of numbers
	:rtype: largest sum of non-adjacent numbers
	"""

	# incl & excl means max sum including and excluding previous no.
	incl, excl = 0, 0
	# Looping through every number
	for no in a:
		temp = excl
		# Calculating excl for next no.
		excl = max(incl, excl)
		# Calculating excl for next no.
		incl = temp + no

	return max(prev_prev_sum, prev_sum)

if __name__ == "__main__":
	print(largest_sum([2, 8, 5]))