import heapq

from typing import List

def merge_k_sorted_list(sorted_k_list: List[List[int]]) -> List[int]:
	"""
	This function will merge k sorted list into a single sorted list.

	:param sorted_k_list: k sorted list
	:rtpye: single sorted list
	"""

	# Getting the value of k
	k = len(sorted_k_list)

	# Initializing our min-heap with k smallest elements
	min_heap = [(sorted_k_list[list_index][0], list_index, 0) for list_index in range(k) if len(sorted_k_list[list_index]) > 0]
	heapq.heapify(min_heap)

	final_sorted_list = []
	while len(min_heap) > 0:
		# Popping out smallest element from the heap
		min_value, list_index, ele_index = heapq.heappop(min_heap)
		# Adding minimum value to the final sorted list
		final_sorted_list.append(min_value)
		# Adding the next smallest element to the heap if available
		if ele_index < len(sorted_k_list[list_index]) - 1:
			heapq.heappush(min_heap, (sorted_k_list[list_index][ele_index+1], list_index, ele_index+1))

	return final_sorted_list

if __name__ == "__main__":
	sorted_k_list = [[1], [1, 3, 5], [1, 10, 20, 30, 40]]
	print(merge_k_sorted_list(sorted_k_list))