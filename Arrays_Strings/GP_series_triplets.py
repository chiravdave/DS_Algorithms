'''
Find all triplets in a sorted array that forms Geometric Progression
Input: arr = [1, 2, 6, 10, 18, 54]
Output: 2 6 18
        6 18 54
'''

class GPTriplets():
	
	def __init__(self, a):
		self.a = a

	def find_gp_triplets(self):
		l = len(self.a)
		for mid in range(1, l-1):
			low = mid - 1
			high = mid + 1
			while low >= 0 and high < l:
				if self.a[mid] % self.a[low] == 0 and self.a[high] % self.a[mid] == 0 and self.a[mid]/self.a[low] == self.a[high]/self.a[mid]:
					print(self.a[low], self.a[mid], self.a[high])
					low -= 1
					high += 1
				elif self.a[mid]/self.a[low] > self.a[high]/self.a[mid]:
					high += 1
				else:
					low -= 1

if __name__ == '__main__':
	ob = GPTriplets([1, 2, 6, 10, 18, 54])
	ob.find_gp_triplets()