'''
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two 
directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a 
path for the robot from the top left to the bottom right.
'''

from collections import deque
from copy import deepcopy

class RobotInAGrid:

	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols

	def find_path_iter(self):
		'''
		Simple BFS Search
		'''
		closed = set()
		fringe = deque()
		start = (1,1,[])
		fringe.append(start)
		while(len(fringe) != 0):
			row, col, path = fringe.popleft()
			if row == self.rows and col == self.cols:
				return path
			closed.add((row,col))
			if row+1 <= self.rows and (row+1, col) not in closed:
				new_path = deepcopy(path)
				new_path.append('down')
				child = (row+1, col, new_path)
				fringe.append(child)
			if col+1 <= self.cols and (row, col+1) not in closed:
				new_path = deepcopy(path)
				new_path.append('right')
				child = (row, col+1, new_path)
				fringe.append(child)

	def find_path_recur(self, curRow, curCol, closed, path):
		'''
		Simple BFS Search
		'''
		if curRow == self.rows and curCol == self.cols:
			return path
		else:
			closed.add((curRow,curCol))
		if curRow+1 <= self.rows and (curRow+1, curCol) not in closed:
			new_path = deepcopy(path)
			new_path.append('down')
			return self.find_path_recur(curRow+1, curCol, closed, new_path)
		if curCol+1 <= self.cols and (curRow, curCol+1) not in closed:
			new_path = deepcopy(path)
			new_path.append('right')
			return self.find_path_recur(curRow, curCol+1, closed, new_path)

	def how_many_paths_iter(self):
		paths = {}
		for row in range(1, self.rows+1):
			for col in range(1, self.cols+1):
				if row == 1 and col == 1:
					paths[(1, 1)] = 1
				else:
					paths[(row, col)] = 0
					#Path from left side
					if row-1 >= 1:
						paths[(row, col)] = paths[(row, col)] + paths[(row-1, col)]
					#Path from top
					if col-1 >= 1:
						paths[(row, col)] = paths[(row, col)] + paths[(row, col-1)]
		return paths[(self.rows, self.cols)]  

	def how_many_paths_recur(self, curRow, curCol, visited):
		if curRow == 1 and curCol == 1:
			return 1
		else:
			if (curRow, curCol) in visited:
				return visited[(curRow, curCol)]
		paths_from_left = 0
		paths_from_up = 0
		#Path from left side
		if curRow-1 >=1:
			paths_from_left =  self.how_many_paths_recur(curRow-1, curCol, visited)
		#Path from top
		if curCol-1 >=1:
			paths_from_up =  self.how_many_paths_recur(curRow, curCol-1, visited)
		total_paths = paths_from_up + paths_from_left
		visited[(curRow, curCol)] = total_paths
		return total_paths

def main():
	rows = int(input("Enter no of rows"))
	cols = int(input("Enter no of columns"))
	robot = RobotInAGrid(rows, cols)
	print("Enter 1 to find a path iteratively or 2 for recursively, 3 for finding no of paths iteratively or 4 for recursively and 5 to exit")
	while(True):
		choice = input("Enter your choice")
		if choice == "1":
			path = robot.find_path_iter()
			print(path)
		elif choice == "2":
			path = robot.find_path_recur(1, 1, set(), [])
			print(path)
		elif choice == "3":
			paths = robot.how_many_paths_iter()
			print(paths)
		elif choice == "4":
			paths = robot.how_many_paths_recur(rows, cols, {})
			print(paths)
		elif choice == "5":
			exit()

if __name__ == "__main__":
	main()