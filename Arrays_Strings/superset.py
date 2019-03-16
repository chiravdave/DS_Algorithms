''' 
Super Set: Given an array of characters, write a method to print all possible sets out of them 
Input: [a,b]
Output: [], [a], [b], [ab]
'''

class SuperSet:

	def __init__(self, a):
		self.a = a

	def print_superset(self):
		self.print_recursively([], 0)

	def print_recursively(self, cur_subset, index):
		if index == len(self.a):
			print(cur_subset)
		else:
			cur_subset.append(self.a[index])
			self.print_recursively(cur_subset, index+1)
			cur_subset.pop()
			self.print_recursively(cur_subset, index+1)

if __name__ == '__main__':
	ob = SuperSet(['a', 'b', 'c', 'd'])
	print('The super set of the given set is:')
	ob.print_superset()