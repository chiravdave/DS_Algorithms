''' 
Given an array of elements. 
1) The task is to find all unique triplets whose sum is equal to a given no.
2) The task is to find a triplets whose sum is closest to a given no
'''

class Triplets:

	def __init__(self, a):
		self.a = a

	def find_all_triplets(self, s):
		#Sort the array
		self.a.sort()
		pairs = set()
		l = len(self.a)
		#Fix each element at a time and then perform 2Sum approach with sum as s-fixed element
		for start in range(l-2):
			new_s = s - self.a[start]
			mid = start+1
			end = l-1
			#Logic of 2Sum
			while mid < end:
				add = self.a[mid] + self.a[end] 
				if add == new_s:
					pairs.add((self.a[start], self.a[mid], self.a[end]))
					end -= 1
					mid += 1
				elif add > new_s:
					end -= 1
				else:
					mid += 1
		print(pairs)

	def find_closest_triplet(self, s):
		closest_sum = 999999
		pair = None
		l = len(self.a)
		for start in range(l-2):
			#Saving time
			if closest_sum == 0:
				break
			new_s = s - start
			mid = start + 1
			end = l - 1
			while mid < end:
				add = self.a[mid] + self.a[end]
				diff = new_s - add
				if abs(diff) < closest_sum:
					closest_sum = abs(diff)
					pair = (self.a[start], self.a[mid], self.a[end])
					#Saving time
					if closest_sum == 0:
						break
				elif diff >= 0:
					mid += 1
				else:
					end -= 1
		print(pair)

if __name__ == '__main__':
	ob = Triplets([0, 0, 0])
	print('All possible triplets that sum to {} are as follows:'.format(0))
	ob.find_all_triplets(0)
	print('The closest triplet to {} is:'.format(0))
	ob.find_closest_triplet(2)