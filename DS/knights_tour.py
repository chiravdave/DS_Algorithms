'''
A knight's tour is a sequence of moves by a knight on a chessboard such that all squares are visited once.

Given N, write a function to return the number of knight's tours on an N by N chessboard. 
'''

from typing import Tuple

class knight:

	def __init__(self, N: int):
		"""
		:param: size of the chessboard
		"""

		self.N = N
		self.n_tours = 0

	def no_of_tours(self) -> int:
		'''
		This method will calculate number of knight's tours on an N X N chessboard.

		
		:rtype: no. of possible tours
		'''

		if self.N <=2:
			return 0

		# This will store cells that has already been visited
		visited = set()
		visited.add((0, 0))
		self._n_tours((0, 0), visited, 1)
		return self.n_tours

	def _n_tours(self, cur_cell: Tuple[int, int], visited: set, cells_visited: int):
		"""
		This method will check for all the possible tours.

		:cur_cell: current cell under examination
		:visited: cells that has already been visited
		:cells_visited: count of cells that have already been visited
		"""

		if cells_visited == self.N * self.N:
			self.n_tours += 1

		else:
			cur_row, cur_col = cur_cell
			# Will try to move our knight to all the possible cells from the current cell
			for double_step in range(-2, 3, 4):
				for single_step in range(-1, 2, 2):
					if cur_row+double_step in range(0, self.N) and cur_col+single_step in range(0, self.N):
						next_cell = (cur_row+double_step, cur_col+single_step)
						if next_cell not in visited:
							visited.add(next_cell)
							self._n_tours(next_cell, visited, cells_visited+1)
							visited.remove(next_cell)

					if cur_row+single_step in range(0, self.N) and cur_col+double_step in range(0, self.N):
						next_cell = (cur_row+single_step, cur_col+double_step)
						if next_cell not in visited:
							visited.add(next_cell)
							self._n_tours(next_cell, visited, cells_visited+1)
							visited.remove(next_cell)

if __name__ == "__main__":
	N = 5
	knight_ob = knight(N)
	print("No. of possible knight's tour on an {} X {} chessboard is: {}".format(N, N, knight_ob.no_of_tours()))