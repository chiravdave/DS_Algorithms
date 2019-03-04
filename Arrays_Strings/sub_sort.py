''' 
Sub Sort: Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n , the entire array would be 
          sorted. Minimize n - m (that is, find the smallest such sequence). 
Input: 1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19
Output: (3, 9) 
'''

class SubSort:

	def __init__(self, a):
		self.a = a

	def get_max_min(self, start, end):
		maximum = self.a[start]
		minimum = self.a[start]
		start = start + 1
		while(start <= end):
			if(self.a[start] > maximum):
				maximum = self.a[start]
			if(self.a[start] < minimum):
				minimum = self.a[start]
			start = start + 1
		return maximum, minimum

	def sub_sort(self):
		length = len(self.a)
		left_end = 0       #Storing end index of the left sorted part
		right_start = length-1  #Storing start index of the right sorted part
		while(left_end < (length-1)):
			if(self.a[left_end] > self.a[left_end+1]):
				break
			left_end = left_end + 1
		#list is already sorted
		if(left_end == (length-1)):
			return((-1,-1))
		while(right_start > left_end):
			if(self.a[right_start] < self.a[right_start-1]):
				break
			right_start = right_start - 1
		#Get max and min from the middle part of the array
		mid_max, mid_min = self.get_max_min(left_end+1, right_start-1)
		start_index = left_end
		end_index = right_start
		#Finding starting index
		while(start_index >=0 and self.a[start_index] > mid_min):
			start_index = start_index - 1
		#Finding end index
		while(end_index < length and self.a[end_index] < mid_max):
			end_index = end_index + 1
		if start_index == -1:
			start_index = 0
		if end_index == length:
			end_index = length - 1
		return start_index, end_index-1

if __name__ == '__main__':
	ob = SubSort([1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19])
	print('The unsorted range is : {}'.format(ob.sub_sort()))