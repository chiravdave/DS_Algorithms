"""
The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a 
Monte Carlo method.

We will assume a circle inside a square with side as 1 unit. Pi will be calculated
as follows:

area of circle / area of square = no. of generated points inside the circle) / 
		no. of generated points inside the square

or, Pi = (4 * no. of generated points inside the circle) / no. of generated points 
		inside the square
"""

import time
from numpy.random import uniform

def estimate_pi(iterations: int) -> int:
	"""

	:param iter: no. of iterations for the simulation
	:rtype: estimated value of pi
	"""

	n_circle_points, n_square_points = 0, 0
	for i in range(1, iterations+1):
		# Sampling a point inisde the square
		sample_x = uniform()
		sample_y = uniform()
		# Checking if the point lies inside the circle
		if pow(sample_x, 2) + pow(sample_y, 2) <= 1:
			n_circle_points += 1
		n_square_points += 1
		
		if i % 50 == 0:
			pi = 4 * (n_circle_points / n_square_points)
			print("Estimated value of pi after {} iterations is: {}".format(i, pi))
			time.sleep(3)

	return pi

if __name__ == "__main__":
	final_pi = estimate_pi(1000)
	print("Final value of pi is: {}".format(final_pi))