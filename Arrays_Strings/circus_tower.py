'''
Circus Tower: A circus is designing a tower routine consisting of people standing on top of one another's shoulders. For practical and aesthetic reasons, 
each person must be both shorter and lighter than the person below him or her. Given the heights and weights of each person in the circus, write a method 
to compute the largest possible number of people in such a tower
'''

class Person:

	def __init__(self, height, weight):
		self.height = height
		self.weight = weight

class CircusTower:

	def __init__(self, people):
		self.people = people

	def get_largest_no(self):
		length = len(self.people)
		#Sorting people with respect to their weight (primary parameter) and height (secondary parameter)
		for i in range(length):
			index = i
			for j in range(i+1,length):
				if(self.people[index].weight < self.people[j].weight) and (self.people[index].height < self.people[j].height):
					index = j
			if(i != index):
				temp = self.people[i]
				self.people[i] = self.people[j]
				self.people[j] = temp
		memo = {length-1:1} #Storing max length starting from the index of every individual person
		largest = 1
		for i in range(length-2,-1,-1):
			max_length = 1
			for j in range(i+1,length):
				if((self.people[i].height > self.people[j].height) and (self.people[i].weight > self.people[j].weight) and (memo[j]+1 > max_length)):
					max_length = memo[j] + 1
			memo[i] = max_length
			if(max_length > largest):
				largest = max_length
		return largest

if __name__ == '__main__':
	n_person = int(input("Enter how many people"))
	people = []
	for i in range(n_person):
		height = int(input("Enter height"))
		weight = int(input("Enter weight"))
		people.append(Person(height, weight))
	circus = CircusTower(people)
	print('Largest Possible No. is: {}'.format(circus.get_largest_no()))