'''
Write a function that takes in an integer and returns the number of ones set in the binary representation.  
'''

class Bits:

	def __init__(self, n):
		self.n = n

	def find_set_bits(self):
		total = 0
		while(self.n != 0):
			res = self.n & 1
			if res == 1:
				total += 1
			self.n = self.n >> 1
		print('No of set bits are: {}'.format(total))

if __name__ == '__main__':
	ob = Bits(20)
	ob.find_set_bits()