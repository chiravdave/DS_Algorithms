'''
WAP to perform the following tasks on a Binary Search Tree:
1) Find in-order successor.
2) Find first common ancester.
'''

class Node:

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BST:

	def __init__(self, root):
		self.root = root

	def search_leftmost_rightsubtree(self, cur_node):
		if not cur_node.left:
			return cur_node.val
		else:
			return self.search_leftmost_rightsubtree(cur_node.left)

	def helper_inorder_successor(self, val, cur_node, successor):
		if not cur_node:
			return cur_node
		elif cur_node.val == val:
			if successor:
				return successor.val
			#Search leftmost node in the right sub tree if present
			elif cur_node.right:
				return self.search_leftmost_rightsubtree(cur_node.right)
			#No in-order successor (rightmost node in the tree)
			else:
				return None
		elif cur_node.val > val:
			return self.helper_inorder_successor(val, cur_node.left, cur_node)
		else:
			return self.helper_inorder_successor(val, cur_node.right, successor)

	def get_inorder_successor(self, val):
		return self.helper_inorder_successor(val, self.root, None)

	def helper_first_common_ancester(self, cur_node, low_val, high_val):
		if not cur_node:
			return None
		#Ancester's value will be in between the two nodes
		elif low_val <= cur_node.val and cur_node.val <= high_val:
			return cur_node.val
		elif low_val > cur_node.val:
			return self.helper_first_common_ancester(cur_node.right, low_val, high_val)
		else:
			return self.helper_first_common_ancester(cur_node.left, low_val, high_val)

	def get_first_common_ancester(self, val_1, val_2):
		if val_1 <= val_2:
			return self.helper_first_common_ancester(self.root, val_1, val_2)
		else:
			return self.helper_first_common_ancester(self.root, val_2, val_1)

def main():
	root = Node(11)
	root.left, root.right = Node(8), Node(15)
	root.left.right = Node(10)
	root.right.right = Node(20)
	root.left.right.left = Node(9)
	root.right.right.left = Node(18)
	tree = BST(root)
	print('The inorder successor of {} is: {}'.format(15, tree.get_inorder_successor(15)))
	print('The first common ancestor of {} and {} is: {}'.format(18, 9, tree.get_first_common_ancester(18, 9)))

if __name__ == "__main__":
	main()