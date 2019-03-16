'''
Permutations: Given a string of characters, write a method to print all possible permutations 
Input: 'abc'
Output: 'abc', 'acb', 'bac', 'bca', 'cba', 'cab'
'''

class Permutations:

	def __init__(self, s):
		#Converting into a list because string is immutable
		self.a = [ch for ch in s]

	def print_string(self):
		print ''.join(self.a)

	def print_permutations(self):
		self.print_permutations_helper(0)

	def print_permutations_helper(self, index):
		l = len(self.a)
		if index == l:
			self.print_string()
		else:
			for i in range(index, l):
				#Swap current indexed element with rest of the elements coming after this index
				self.a[index], self.a[i] = self.a[i], self.a[index]
				self.print_permutations_helper(index+1)
				#Backtrack to previous state in the recursion tree
				self.a[index], self.a[i] = self.a[i], self.a[index]

if __name__ == '__main__':
	ob = Permutations('abc')
	ob.print_permutations()