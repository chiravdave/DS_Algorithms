"""
WAP to implement an efficient sudoku solver. Sudoku is a puzzle where you're given a partially-filled 9 by 9 
grid with digits. The objective is to fill the grid with the constraint that every row, column, and box 
(3 by 3 subgrid) must contain all of the digits from 1 to 9.
"""

from typing import List

class Sudoku:

	def __init__(self, board: List[List[int]]):
		"""
		:param board: initial board configuration
		"""

		self.board = board

	def _check_block(self, no: int, cur_row: int, cur_col: int) -> bool:
		"""
		This method will check if the number can be put within the current block.

		:param no: no. to check against
		:param cur_row: row of the current block under examination
		:param cur_col: column of the current block under examination
		:rtype: if the number can be put within the current block.
		"""

		start_row, start_col = cur_row-cur_row%3, cur_col-cur_col%3
		for row in range(start_row, start_row+3):
			for col in range(start_col, start_col+3):
				if row != cur_row and col != cur_col and self.board[row][col] == no:
					return False
		return True

	def _check_row(self, no: int, cur_row: int, cur_col: int) -> bool:
		"""
		This method will check if the number can be put in the current row.

		:param no: no. to check against
		:param cur_row: current row under examination
		:param cur_col: current col under examination
		:rtype: if the number can be put in the current row.
		"""

		for col in range(9):
			if col != cur_col and self.board[cur_row][col] == no:
				return False
		return True

	def _check_col(self, no: int, cur_row: int, cur_col: int) -> bool:
		"""
		This method will check if the number can be put in the current column.

		:param no: no. to check against
		:param cur_row: current row under examination
		:param cur_col: current col under examination
		:rtype: if the number can be put in the current column.
		"""

		for row in range(9):
			if row != cur_row and self.board[row][cur_col] == no:
				return False
		return True

	def _solve(self, cur_row: int, cur_col: int) -> bool:
		"""
		This method will try to fill every possible cell in the board.

		:param cur_row: current row under examination
		:param cur_col: current col under examination
		:rtype: if current cell in the board can take a no. 
		"""

		# Checking if we have visited all the cells in the board
		if cur_row == 9:
			return True

		# Checking if the current cell has a value or not
		if self.board[cur_row][cur_col] != 0:
			if cur_col == 8:
				return self._solve(cur_row+1, 0)
			else:
				return self._solve(cur_row, cur_col+1)

		for no in range(1, 10):
			if self._check_row(no, cur_row, cur_col) and self._check_col(no, cur_row, cur_col) \
				and self._check_block(no, cur_row, cur_col):
				self.board[cur_row][cur_col] = no
				check = False
				# Checking if we have completed current row
				if cur_col == 8:
					check = self._solve(cur_row+1, 0)
				# Moving to the next column in the current row
				else:
					check = self._solve(cur_row, cur_col+1)
				# Checking if we the current value is valid
				if check:
					return True
		# No value could be assigned to the current cell
		self.board[cur_row][cur_col] = 0
		return False

	def solve(self) -> bool:
		"""
		This method will try to solve the game.

		:rtype: whether the game can be solved or not
		"""

		return self._solve(0, 0)

	def print_board(self) -> None:
		"""
		This method will print the current configuration of the board.
		"""

		for row in range(9):
			for col in range(9):
				print(self.board[row][col], end=" ")
			print()

if __name__ == "__main__":
	board=[
			[3,0,6,5,0,8,4,0,0],
			[5,2,0,0,0,0,0,0,0], 
			[0,8,7,0,0,0,0,3,1], 
			[0,0,3,0,1,0,0,8,0], 
			[9,0,0,8,6,3,0,0,5], 
			[0,5,0,0,9,0,6,0,0], 
			[1,3,0,0,0,0,2,5,0], 
			[0,0,0,0,0,0,0,7,4], 
			[0,0,5,2,0,6,3,0,0]
		]
	game = Sudoku(board)
	solved = game.solve()
	if solved:
		print("Game is solved")
		game.print_board()
	else:
		print("Game cannot be solved")