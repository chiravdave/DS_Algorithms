''' 
Letters and Numbers: Given an array filled with letters and numbers, find the longest subarray with an equal number of letters and numbers.
'''

class LettersNumbers:

	def __init__(self, a):
		self.a = a

	def equal_lets_nos(self):
		'''
		This function will store count of nos seen till a particular index value inside a dictionary and if it finds an entry already 
		present inside the dictionary or if the count of nos is 0, it will update the max_size value of the longest subarray with equal 
		number of letters and numbers.
		'''
		count_nos = {}    #Dictionary to store the index of differences observed for the first time
		count_no = 0
		max_size = 0
		low_index, high_index = -1,-1
		for i in range(len(self.a)):
			if self.a[i]>=0 and self.a[i]<=9:
				count_no = count_no + 1
			else:
				count_no = count_no - 1
			if count_no == 0 and max_size<(i+1):
				max_size = i+1
				low_index = 0
				high_index = i + 1
			else:
				if count_no not in count_nos:
					count_nos[count_no] = i
				elif (i - count_nos[count_no]) > max_size:
					max_size = i - count_nos[count_no]
					low_index = count_nos[count_no] + 1
					high_index = i + 1
		if max_size == 0:
			return []
		else:
			return self.a[low_index:high_index]

if __name__ == '__main__':
	let_num = LettersNumbers(['y',1,'d','c','d',2,3,4])
	print 'Longest subarray with equal no of letters and numbers is :', let_num.equal_lets_nos()