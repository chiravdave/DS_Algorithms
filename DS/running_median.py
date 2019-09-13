"""
Compute the running median of a sequence of positive numbers. That is, given a stream of positive 
numbers, print out the median of the list so far on each new element.
"""

import heapq
from typing import List

def running_median(nums: List[int]) -> List[int]:
	"""
	This function will return running median of a sequence of positive numbers.

	:param nums: sequence of positive numbers
	:rtype: running median
	"""

	min_heap, max_heap =  [], []
	# Let's turn these list into min-heap
	heapq.heapify(min_heap)
	heapq.heapify(max_heap)
	# Current median will help us to insert the new element
	cur_median = None
	n_left_nodes, n_right_nodes = 0, 0
	
	result = []
	for no in nums:
		if cur_median:
			# Adding the new no. to min heap if it is equal to or less than current median 
			if no <= cur_median:
				heapq.heappush(max_heap, no * -1)
				n_left_nodes += 1
			# Adding the new no. to max heap if it is greater than current median
			else:
				# Negating the value as we are using a min heap to behave like max heap
				heapq.heappush(min_heap, no)
				n_right_nodes += 1

		else:
			heapq.heappush(max_heap, no * -1)
			n_left_nodes += 1

		# Checking if we have balanced heaps
		if abs(n_left_nodes - n_right_nodes) > 1:
			if n_left_nodes > n_right_nodes:
				pop_no = heapq.heappop(max_heap) * -1
				n_left_nodes -= 1
				heapq.heappush(min_heap, pop_no)
				n_right_nodes += 1
			else:
				pop_no = heapq.heappop(min_heap)
				n_right_nodes -= 1
				heapq.heappush(max_heap, pop_no * -1)
				n_left_nodes += 1

		# Calculating median
		if (n_left_nodes + n_right_nodes) % 2 == 0:
			cur_median = (max_heap[0] * -1 + min_heap[0]) / 2
		elif n_left_nodes > n_right_nodes:
			cur_median = max_heap[0] * -1
		else:
			cur_median = min_heap[0]

		result.append(cur_median)

	return result
			
if __name__ == "__main__":
	print("Running median is as follow:")
	print(running_median([5, 15, 1, 3, 2, 8, 7, 9, 10, 6, 11, 4]))