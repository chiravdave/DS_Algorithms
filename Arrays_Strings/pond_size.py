''' 
Pond Sizes: You have an integer matrix representing a plot of land, where the value at that location represents the height above sea level. A value of 
            zero indicates water. A pond is a region of water connected vertically, horizontally, or diagonally. The size of the pond is the total number 
            of connected water cells. Write a method to compute the sizes of all ponds in the matrix.
Input:
      0 2 1 0
      0 1 0 1
      1 1 0 1
      0 1 0 1      
Output: 2, 4, 1 (in any order)
'''
from collections import deque

class Pond:

	def __init__(self, plot):
		self.plot = plot

	def get_pond_depth(self, row, col, rows, cols):
		'''
		This function will give the maximum stretch of a given pond. Once a pond is visited, change it's value to -1 so that we don't consider it again
		in future.
		'''
		depth = 1
		queue = deque()
		queue.append((row, col))
		self.plot[row][col] = -1
		while(len(queue) > 0):
			row, col = queue.pop()
			#Checking top left neighbor
			if(row>0 and col>0 and (self.plot[row-1][col-1] == 0)):
				self.plot[row-1][col-1] = -1
				depth = depth + 1
				queue.append((row-1, col-1))
			#Checking top neighbor
			if(row>0 and (self.plot[row-1][col] == 0)):
				self.plot[row-1][col] = -1
				depth = depth + 1
				queue.append((row-1, col))
			#Checking top right neighbor
			if(row<0 and (col+1)<cols and (self.plot[row-1][col+1] == 0)):
				self.plot[row-1][col+1] = -1
				depth = depth + 1
				queue.append((row-1, col+1))
			#Checking left neighbor
			if(col>0 and (self.plot[row][col-1] == 0)):
				self.plot[row][col-1] = -1
				depth = depth + 1
				queue.append((row, col-1))
			#Checking right neighbor
			if((col+1)<cols and (self.plot[row][col+1] == 0)):
				self.plot[row][col+1] = -1
				depth = depth + 1
				queue.append((row, col+1))
			#Checking bottom left neighbor
			if((row+1)<rows and col>0 and (self.plot[row+1][col-1] == 0)):
				self.plot[row+1][col-1] = -1
				depth = depth + 1
				queue.append((row+1, col-1))
			#Checking bottom neighbor
			if((row+1)<rows and (self.plot[row+1][col] == 0)):
				self.plot[row+1][col] = -1
				depth = depth + 1
				queue.append((row+1, col))
			#Checking bottom right neighbor
			if((row+1)<rows and (col+1)<cols and (self.plot[row+1][col+1] == 0)):
				self.plot[row+1][col+1] = -1
				depth = depth + 1
				queue.append((row+1, col+1))
		return depth

	def pond_sizes(self):
		'''
		This function will check for all available ponds
		'''
		sizes = set()
		rows = len(self.plot)
		cols = len(self.plot[0])
		for row in range(rows):
			for col in range(cols):
				if(self.plot[row][col] == 0):
					sizes.add(self.get_pond_depth(row, col, rows, cols))
		return sizes

if __name__ == '__main__':
	pond = Pond([[0,2,1,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]])
	print('The pool sizes are : {}'.format(pond.pond_sizes()))