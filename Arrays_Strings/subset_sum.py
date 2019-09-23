"""
Given a list of integers S and a target number k, write a function that returns a subset of S
that adds up to k. If such a subset cannot be made, then return null. Integers can appear more
than once in the list. You may assume all numbers in the list are positive.

Input: S = [12, 1, 61, 5, 9, 2] and k = 24
Output: [12, 9, 2, 1] since it sums up to 24.
"""

from typing import List, Optional

class SubsetSum:

	def __init__(self, nums: List[int]):
		self.nums = nums
		self.max_sum = 50
		self._build_table()

	def _build_table(self) -> None:
		"""
		This method will build a table to the max sum and we will query this table to get our 
		results/subsets.
		"""

		rows = len(self.nums)
		# Initializing table values
		self.table = [[False]*(self.max_sum+1) for row in range(rows)]

		for row in range(rows):
			for col in range(self.max_sum+1):
				# If target is zero then we will have empty subset
				if col == 0:
					self.table[row][col] = True
				
				# Checking if the current no. is greater the target sum 
				elif self.nums[row] > col:
					if row > 0:
						# Will ignore the current no.
						self.table[row][col] = self.table[row-1][col]
				
				# We can include or ignore the current no. 
				else:
					if row == 0:
						if self.nums[row] == col:
							self.table[row][col] = True
					else:
						self.table[row][col] = self.table[row-1][col] or self.table[row-1][col-self.nums[row]]

	def check_subset(self, target_sum: int) -> Optional[List[int]]:
		"""
		This method will return a subset that adds up to the target sum if possible or none if there is no such 
		possible subset.

		:param target_sum: target sum to be achieved
		:rtype: subset of no.s that can sum up to the target or else none   
		"""

		if target_sum > self.max_sum:
			print("Target sum cannot be greater than {}".format(self.max_sum))
			return None

		rows = len(self.nums)

		# Checking if the target sum is achievable
		for row in range(rows):
			if self.table[row][target_sum] == True:
				break

		if row == rows:
			return None

		subset = []
		while target_sum != 0:
			if row != 0:
				if not self.table[row-1][target_sum]:
					subset.append(self.nums[row])
					target_sum -= self.nums[row]
			else:
				 target_sum -= self.nums[row]
				 subset.append(self.nums[row])

			row -= 1

		return subset

if __name__ == "__main__":
	ob = SubsetSum([6, 1, 5, 20, 25, 4, 12])
	print(ob.check_subset(45))