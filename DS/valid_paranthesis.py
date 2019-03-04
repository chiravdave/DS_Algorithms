'''
Valid Parenthesis: Implement an algorithm to print all valid (i.e., properly opened and closed) combinations of n pairs of parentheses.
'''

class ValidParanthesis:

	def generate_valid_combinations(self, left_remain, right_remain, curr_combination, all_combinations):
		if left_remain == 0 and right_remain == 0:
			all_combinations.append(curr_combination)
		else:
			#Add as much left paranthesis as possible
			if left_remain > 0:
				self.generate_valid_combinations(left_remain-1, right_remain, curr_combination+'(', all_combinations)
			#Add right paranthesis unless it is less than the remaining left paranthesis
			if right_remain > 0 and right_remain-1 >= left_remain:
				self.generate_valid_combinations(left_remain, right_remain-1, curr_combination+')', all_combinations)
		return

def main():
	pairs = int(input("Enter no of of pairs"))
	paranthesis = ValidParanthesis()
	all_combinations = []
	paranthesis.generate_valid_combinations(pairs, pairs, '', all_combinations)
	print(all_combinations) 

if __name__ == "__main__":
	main()