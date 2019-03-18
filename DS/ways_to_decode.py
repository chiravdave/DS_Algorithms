'''
Decode String: Implement an algorithm to find no of ways to decode a string where characters are number from 1 to 26.
Input: "112"
Output: 3 ("aab", "kb", "al")
'''

class Decode:

	def __init__(self, encrypt):
		self.encrypt = encrypt
		self.memo = {}

	def ways_to_decode(self, start_index):
		if start_index == len(self.encrypt):
			return 1
		#No deconding possible if the first no. is a zero 
		elif self.encrypt[start_index] == '0':
			return 0
		elif start_index in self.memo:
			return self.memo[start_index]
		else:
			if start_index+1 < len(self.encrypt) and int(self.encrypt[start_index:start_index+2]) <= 26:
				self.memo[start_index] = self.ways_to_decode(start_index+1) + self.ways_to_decode(start_index+2)
			else:
				self.memo[start_index] = self.ways_to_decode(start_index+1)
			return self.memo[start_index]

def main():
	encrypt = input("Enter the encrypted string")
	decoding = Decode(encrypt)
	print('No of ways to decode the encrypted string {} are: {}'.format(encrypt, decoding.ways_to_decode(0)))

if __name__ == "__main__":
	main()