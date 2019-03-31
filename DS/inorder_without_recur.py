'''
WAP to to perform Inorder Tree Traversal without Recursion
'''

class Node:

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class Inorder:

	def perform_inorder(self, root):
		if not root:
			print('Tree is empty')
			return
		print('Inorder traversal of the given tree is:')
		stack = []
		current_node = root
		l = len(stack)
		while(current_node or l>0):
			#Check if current node exists
			if current_node:
				#Add left child into the stack
				stack.append(current_node)
				current_node = current_node.left
			else:
				#Print last root node
				ele = stack.pop()
				print(ele.val, ' ', end='')
				#Change current node to the right child
				current_node = ele.right
			l = len(stack)
		print()

def main():
	inorder = Inorder()
	root = Node(2)
	root.left = Node(4)
	root.right = Node(1)
	root.left.left = Node(5)
	root.left.right = Node(-3)
	root.left.right.left = Node(0)
	inorder.perform_inorder(root)

if __name__ == "__main__":
	main()