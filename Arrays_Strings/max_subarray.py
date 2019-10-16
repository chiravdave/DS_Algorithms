"""
Given an array of integers and a number k, where 1 <= k <= length of the array, 
compute the maximum values of each subarray of length k.

For example, given array = [10, 5, 2, 7, 8, 7] and k = 3, we should get: [10, 7, 8, 8].
"""

from collections import deque

class MaxSubarray:

	def __init__(self, arr: list):
		self.arr = arr

	def _add(self, temp: list, index: int) -> None:
		"""
		This method will add a no. to maintain k largest no.s inside the current window

		:param temp: current window of k largest elements
		:param index: index of the no. that we are adding
		"""

		new_no = self.arr[index]
		# Largest numbers should be in descending order
		for i in range(len(temp)-1, -1, -1):
			if self.arr[temp[i]] <= new_no:
				temp.pop()

		temp.append(index)

	def find_max_subarrays(self, k: int) -> list:
		"""
		This method will return a list of maximum values for each subarray of length k.

		:param k: window size for the subarray
		:rtype: list of maximum values for each subarray
		"""

		k_largest = deque()
		# Initializing array with k largest elements from the starting window
		for index in range(k-1):
			self._add(k_largest, index)

		output = []
		for index in range(k-1, len(self.arr)):
			self._add(k_largest, index)
			output.append(self.arr[k_largest[0]])
			# Removing the element at the front if it's on the edge of the current window
			if k_largest[0] == (index-k+1):
				k_largest.popleft()

		return output

if __name__ == "__main__":
	max_subarrays = MaxSubarray([8, 5, 10, 7, 9, 4, 15, 12, 90, 13])
	print(max_subarrays.find_max_subarrays(4))