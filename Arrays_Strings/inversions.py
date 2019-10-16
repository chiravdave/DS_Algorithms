"""
Given an array, count the number of inversions it has. Do this faster than O(N^2) time. Two elements A[i] and A[j]
form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element. Ex.

I/P: [2, 4, 1, 3, 5] 
O/P: 3 inversions {(2, 1), (4, 1), and (4, 3)}
"""

from typing import List

class Inversions:

	def __init__(self, nums: List[int]):
		self.nums = nums

	def get_inversions(self	) -> int:
		"""
		This method will count no. of inversions in the input array.

		:rtype: no. of inversions
		"""

		return self._find_inversions(0, len(self.nums) - 1)

	def _find_inversions(self, low: int, high: int) -> int:
		"""
		This method will count no. of inversions in the input array.

		:rtype: no. of inversions
		"""

		if low < high:
			mid = int((low + high) / 2)
			n_left_inversions = self._find_inversions(low, mid)
			n_right_inversions = self._find_inversions(mid+1, high)
			n_merged_inversions = self._merge(low, mid, high)
			return n_merged_inversions + n_left_inversions + n_right_inversions

		else:
			return 0

	def _merge(self, low: int, mid: int, high: int) -> int:
		"""
		This method will count no. of inversions in the merged array.

		:rtype: no. of inversions
		"""

		n_inversions = 0
		temp_sorted_list = []
		i, j = low, mid+1

		while i <= mid and j <= high:
			if self.nums[i] > self.nums[j]:
				n_inversions += mid - i + 1
				temp_sorted_list.append(self.nums[j])
				j += 1
			else:
				temp_sorted_list.append(self.nums[i])
				i += 1

		# Checking if all the elements from the left sub array is processed
		while i <= mid:
			temp_sorted_list.append(self.nums[i])
			i += 1

		# Checking if all the elements from the right sub array is processed
		while j <= high:
			temp_sorted_list.append(self.nums[j])
			j += 1

		# Copying sorted values into the original list
		while high >= low:
			self.nums[high] = temp_sorted_list.pop()
			high -= 1

		return n_inversions

if __name__ == "__main__":
	inversion_ob = Inversions([5, 4, 3, 2, 1])
	print("No. of inversions are: {}".format(inversion_ob.get_inversions()))