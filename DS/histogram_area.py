'''
Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number of contiguous bars.
Assume that all bars have unit width.
Histogram of heights: {6, 2, 5, 4, 5, 1, 6}
Largest rectangle possible is 12 (4*3)
'''

class HistogramArea:

	def __init__(self, heights):
		self.heights = heights

	def max_rectangular_area(self):
		max_area = 0
		stack = []
		l = len(self.heights)
		for i in range(l):
			len_stack = len(stack)
			# Stack will contain elements in increasing order only
			if len_stack == 0 or stack[len_stack-1][1] <= self.heights[i]:
				stack.append((i, self.heights[i]))
			else:
				#The last bar inside the stack cannot cover any further area
				max_area = self.remove_larger_bars(stack, max_area, i)
		if(len(stack) > 0):
			max_area = self.remove_remaining(stack, max_area, i)
		return max_area

	def remove_remaining(self, stack, max_area, cur_index):
		while len(stack) > 0:
			index, value = stack.pop()
			if value*(cur_index-index) > max_area:
				max_area = value*(cur_index-index)
		return max_area

	def remove_larger_bars(self, stack, max_area, cur_index):
		last_index = None
		l = len(stack)
		while True:
			if l == 0 or stack[-1][1] <= self.heights[cur_index]:
				break
			else:
				last_index, value = stack.pop()
				l -= 1
				if value*(cur_index-last_index) > max_area:
					max_area = value*(cur_index-last_index)
		stack.append((last_index, self.heights[cur_index]))
		return max_area

def main():
	histogram = HistogramArea([2, 3, 1, 4])
	print('Largest rectangular area possible in the given histogram is: {}'.format(histogram.max_rectangular_area()))

if __name__ == "__main__":
	main()