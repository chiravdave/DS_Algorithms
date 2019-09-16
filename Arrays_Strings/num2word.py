''' 
Write code to convert a given number into words. Only consider numbers up to 4 digits, i.e., numbers from 0 to 9999. 
I/P: "1234" 
O/P: “one thousand two hundred thirty four". 
'''
from collections import deque

class Number2Words:

	def __init__(self, n):
		self.n = n
		self.units = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
		self.tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
		self.special_tens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

	def convert_to_words(self):
		'''
		This method will generate words corresponding to the give no
		'''
		l = len(self.n)
		index = l-1
		#Handle zero digit separately
		if l == 1 and self.n[0] == '0':
			print('zero')
			return
		result = deque()
		result.appendleft('')
		while index >= 0:
			if self.n[index] != '0':
				# Position will tell us which place we are looking at (units, tens, hundred or thousand)
				position = l - (index + 1)
				if position == 0:
					result.appendleft(self.units[ord(self.n[index]) - 49])
				elif position == 1:
					# Check if this belongs to the special ten case
					if self.n[index] == '1' and self.n[index+1] != '0':
						result.popleft()
						result.appendleft(self.special_tens[ord(self.n[index+1]) - 49])
					else:
						result.appendleft(' ')
						result.appendleft(self.tens[ord(self.n[index]) - 49])
				elif position == 2:
					result.appendleft(' ')
					result.appendleft('hundred')
					result.appendleft(' ')
					result.appendleft(self.units[ord(self.n[index]) - 49])
				else:
					result.appendleft(' ')
					result.appendleft('thousand')
					result.appendleft(' ')
					result.appendleft(self.units[ord(self.n[index]) - 49])
			index -= 1
		print(''.join(result))

if __name__ == '__main__':
	num_words = Number2Words('1105')
	num_words.convert_to_words()