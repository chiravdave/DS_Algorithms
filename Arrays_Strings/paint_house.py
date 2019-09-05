"""
A builder is looking to build a row of N houses that can be of K different colors. He has a goal of minimizing cost
while ensuring that no two neighboring houses are of the same color. Given an N by K matrix where the nth row and kth
column represents the cost to build the nth house with kth color, return the minimum cost which achieves this goal.
"""

from typing import List

def min_paint_cost(house_color_comb: List[List[int]]) -> int:
	"""
	This function will return the minimum cost for coloring houses such that no two neighboring houses are of the
	same color.

	:param house_color_comb: N by K matrix where the nth row and kth column represents the cost to build the nth house
							with kth color
	:rtype: minimum cost for coloring the houses
	"""

	# Finding no. of houses to paint
	rows = len(house_color_comb)
	# Finding no. of colors
	cols = len(house_color_comb[0])
	# Validating input
	if rows<=0 or cols<=1:
		raise Exception("Invalid input. There should be at least one house and two colors")
	# Will store min_cost and second_min_cost to color all houses till now 
	last_min_cost, last_second_min_cost = (-1, 999998), (-1, 999999)
	for col in range(cols):
		if last_min_cost[1] > house_color_comb[0][col]:
			last_min_cost = (col, house_color_comb[0][col])
		elif last_second_min_cost[1] > house_color_comb[0][col]:
			last_second_min_cost > (col, house_color_comb[0][col])

	for row in range(1, rows):
		# To store min_cost and second_min_cost to color all houses including current house
		cur_min_cost, cur_second_min_cost = (-1, 999998), (-1, 999999) 
		for col in range(cols):
			# Finding min cost to paint the current house with current color
			if col != last_min_cost[0]:
				house_color_comb[row][col] += last_min_cost[1]
			else:
				house_color_comb[row][col] += last_second_min_cost[1]

			# Updating current minimum and second minimum cost to color all houses including current house
			if cur_min_cost[1] > house_color_comb[row][col]:
				cur_min_cost = (col, house_color_comb[row][col])
			elif cur_second_min_cost[1] > house_color_comb[row][col]:
				cur_second_min_cost > (col, house_color_comb[row][col])

		# Update previous minimum  and second minimum cost to color all house till now
		last_min_cost, last_second_min_cost = cur_min_cost, cur_second_min_cost

	return min(last_min_cost[1], last_second_min_cost[1])

if __name__ == "__main__":
	print(min_paint_cost([[1,10,3,100,110], [2,5,15,200,220], [7,1,8,300,330], [15,14,13,16,18], [20,21,22,23,24]]))