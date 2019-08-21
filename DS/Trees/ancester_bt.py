'''
First Common Ancestor: Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. 
Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.
'''

class Node:

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BST:

	def __init__(self, root):
		self.root = root

	def helper_first_common_ancester(self, cur_node, val_1, val_2):
		if not cur_node:
			return None
		# Ancester's value will be in between the two nodes
		elif cur_node.val == val_1 or cur_node.val == val_2:
			return cur_node.val
		else:
			left = self.helper_first_common_ancester(cur_node.left, val_1, val_2)
			right = self.helper_first_common_ancester(cur_node.right, val_1, val_2)
			if left and right:
				return cur_node.val
			elif left:
				return left
			else:
				return right

	def get_first_common_ancester(self, val_1, val_2):
		return self.helper_first_common_ancester(self.root, val_1, val_2)

def main():
	root = Node(11)
	root.left, root.right = Node(15), Node(18)
	root.left.right = Node(1)
	root.left.left = Node(2)
	root.right.left = Node(20)
	root.right.left.right = Node(100)
	tree = BST(root)
	print('The first common ancestor of {} and {} is: {}'.format(11, 5, tree.get_first_common_ancester(11, 2)))

if __name__ == "__main__":
	main()