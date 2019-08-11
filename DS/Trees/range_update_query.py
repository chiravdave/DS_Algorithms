from math import log, pow, ceil
from typing import List

class SegmentTree:

	def __init__(self, nums: List[int]):
		self._n = len(nums)
		# Calculate size of the tree
		height = ceil(log(self._n, 2))
		size = int(2 * pow(2, height) - 1)
		self._tree = [0]*size
		self._build_tree(nums, 0, 0, self._n-1)

	def _build_tree(self, nums: List[int], tree_pos: int, low: int, high: int) -> None:
		"""
		This method will build a blanaced binary tree recursively
		"""

		if low == high:
			self._tree[tree_pos] = nums[low]
			return nums[low]

		mid = int((low+high)/2)
		left = self._build_tree(nums, tree_pos*2+1, low, mid)
		right = self._build_tree(nums, tree_pos*2+2, mid+1, high)
		self._tree[tree_pos] = left + right
		return self._tree[tree_pos]

	def update(self, pos: int, val: int) -> None:
		"""
		This method will update an element in the array.
		"""

		# Check if the index is valid
		if pos < 0 or pos >= self._n:
			print("Invalid index should be between 0 and {} (inclusive)".format(self._n-1))
			return

		self._update_helper(pos, val, 0, 0, self._n-1)

	def _update_helper(self, pos: int, val: int, tree_pos: int, low: int, high: int) -> None:
		"""
		This will update values in the tree in bottom to up fashion.
		"""

		if low == high:
			old_value = self._tree[tree_pos]
			self._tree[tree_pos] = val
			return old_value

		mid = int((low+high)/2)
		if pos <= mid:
			old_value = self._update_helper(pos, val, tree_pos*2+1, low, mid)
		else:
			old_value = self._update_helper(pos, val, tree_pos*2+2, mid+1, high)

		self._tree[tree_pos] += val - old_value
		return old_value

	def find_sum(self, i: int, j: int) -> int:
		"""
		This method will return sum of the elements within the given range.
		"""

		# Check if the range is valid
		if i < 0 or j >= self._n or i > j:
			print("Invalid range should be between 0 and {} (inclusive)".format(self._n-1))
			return

		return self._find_sum_helper(0, i, j, 0, self._n-1)

	def _find_sum_helper(self, tree_pos: int, i: int, j:int, low: int, high: int) -> int:
		"""
		This method will traverse the tree in different branches to obtain the required sum.
		"""

		# Check if the given current array range is inside the given range
		if i <= low and high <= j:
			return self._tree[tree_pos]
		# Check if there is no overlap between the given and current array range
		elif j < low or i > high:
			return 0
		# This means there is an overlap between the given and current array range
		else:
			mid = int((low+high)/2)
			left = self._find_sum_helper(tree_pos*2+1, i, j, low, mid)
			right = self._find_sum_helper(tree_pos*2+2, i, j, mid+1, high)
			return left+right

if __name__ == "__main__":
	nums = [1, 3, 5, 7, 9, 11]
	tree_ob = SegmentTree(nums)
	print(tree_ob._tree)
	while True:
		choice = int(input("Enter 1 to update a value in the tree, 2 to find sum of elements within a range or 3 to exit: "))
		if choice == 1:
			pos, val = map(int, input("Enter the index and value of the array to update: ").split())
			tree_ob.update(pos, val)

		elif choice == 2:
			i, j = map(int, input("Enter the range of the array whose sum you want to know: ").split())
			print(tree_ob.find_sum(i, j))
	
		elif choice == 3:
			exit()

		else:
			print("Wrong Choice!")