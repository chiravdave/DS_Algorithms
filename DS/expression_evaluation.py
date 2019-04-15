'''
WAP to evaluate a mathematical expression following the BODMAS rule. Ex

I/P : 2 + 5 * 4 - 3
O/P : 19
'''

class EvaluateExpression:

	def __init__(self):
		self.operator_precedence = {'*':1, '/':1, '+':0, '-':0}

	def infix_evaluation(self, exp):
		'''
		This method will evaluate the given infix expression
		'''
		output_stack, operator_stack, no = [], [], []
		for ch in exp:
			if ch in self.operator_precedence:
				output_stack.append(float(''.join(no)))
				no = []
				self.update_operator_stack(ch, operator_stack, output_stack)
			else:
				no.append(ch)
		#Adding last number
		output_stack.append(float(''.join(no)))
		if len(operator_stack) > 0:
			self.empty_operator_stack(operator_stack, output_stack)
		return output_stack.pop()

	def update_operator_stack(self, op, operator_stack, output_stack):
		'''
		This method will store intermediate result of the given expression
		'''
		l = len(operator_stack)
		while l > 0 and self.operator_precedence[op] <= self.operator_precedence[operator_stack[-1]]:
			operator = operator_stack.pop()
			operand2 = output_stack.pop()
			operand1 = output_stack.pop()
			l -= 1
			if operator == '*':
				output_stack.append(operand1 * operand2)
			elif operator == '/':
				output_stack.append(operand1 / operand2 )
			elif operator == '+':
				output_stack.append(operand1 + operand2)
			else:
				output_stack.append(operand1 - operand2)
		operator_stack.append(op)

	def empty_operator_stack(self, operator_stack, output_stack):
		l = len(operator_stack)
		while l > 0:
			operator = operator_stack.pop()
			operand2 = output_stack.pop()
			operand1 = output_stack.pop()
			l -= 1
			if operator == '*':
				output_stack.append(operand1 * operand2)
			elif operator == '/':
				output_stack.append(operand1 / operand2 )
			elif operator == '+':
				output_stack.append(operand1 + operand2)
			else:
				output_stack.append(operand1 - operand2)			

if __name__ == "__main__":
	infix_exp = EvaluateExpression()
	exp = '2+2-3/3*4'
	print('The infix evaluation of {} is = {}'.format(exp, infix_exp.infix_evaluation(exp))) 