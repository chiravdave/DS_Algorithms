'''
Circus Tower: A circus is designing a tower routine consisting of people standing on top of one another's shoulders. For practical and aesthetic reasons, 
each person must be both shorter and lighter than the person below him or her. Given the heights and weights of each person in the circus, write a method 
to compute the largest possible number of people in such a tower
'''

from typing import List, Tuple

class Person:

	def __init__(self, height: int, weight: int):
		self.height = height
		self.weight = weight

	def __lt__(self, other_person):
		return self.height < other_person.height

	def __str__(self):
		return "Height & Weight are : {} and {}".format(self.height, self.weight)

class CircusTower:

	def __init__(self, people: List[Tuple[int, int]]):
		self.people = people

	def show_all(self) -> None:
		"""
		This method will display the list of people
		"""

		for index, person in enumerate(self.people):
			print("Property of person at index {} is: {}".format(index, person))

	def get_largest_no(self) -> int:
		"""
		This method will return the largest possible number of people in this tower.

		:param people: list of people with their height and weight
		:rtype: largest possible number of people in this tower
		"""

		# Sorting people with respect to their height
		self.people.sort()
		#self.show_all()
		# Now we just need to find the highest increasing subsequence respect to the weight values 
		n_person = len(self.people)
		# Will store the max lenght of increasing subsequence found till each index
		largest_ss = [1] * n_person
		final_subsequence = 1
		for start in range(n_person):
			for prev in range(start):
				# Comparing height betwee two person
				if self.people[prev].weight >= self.people[start].weight and (largest_ss[prev] + 1) > largest_ss[start]:
					 largest_ss[start] = largest_ss[prev] + 1
					 # Will calculate the highest increasing subsequence as well
					 if final_subsequence < largest_ss[start]:
					 	final_subsequence = largest_ss[start]

		return final_subsequence


if __name__ == "__main__":
	n_person = int(input("Enter how many people"))
	people = []
	for i in range(n_person):
		print("Enter details for person {}".format(i+1))
		height = int(input("Enter height"))
		weight = int(input("Enter weight"))
		people.append(Person(height, weight))
	circus = CircusTower(people)
	print("Largest Possible No. is: {}".format(circus.get_largest_no()))