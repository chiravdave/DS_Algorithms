'''
Given pre-order and in-order traversals of a binary tree, write a function to reconstruct the tree.

I/P:	Preorder traversal: [a, b, d, e, c, f, g]
		Inorder traversal: [d, b, e, a, f, c, g]

O/P:	a
	   / \
	  b   c
	 / \ / \
	d  e f  g
'''

class Node:

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class ConstructBT:

	def __init__(self):
		self.root = None
		self.preorder_index = 0

	def construct_tree(self, preorder: list, inorder: list) -> None:
		"""
		This method will construct binary tree using preorder and inorder traversals.

		:param preorder: preorder traversal of the tree
		:param inorder: inorder traversal of the tree
		"""

		if not preorder or not inorder:
			return

		self.preorder_index = 0
		self._building(preorder, inorder, 0, len(inorder)-1)

	def _building(self, preorder, inorder, low, high):
		"""
		This method will construct binary tree using preorder and inorder traversals.

		:param preorder: preorder traversal of the tree
		:param inorder: inorder traversal of the tree
		:param low: starting of the left subtree for current root node
		:param high: ending of the right subtree for the current root node
		"""

		if low > high:
			return None

		else:
			cur_root = Node(preorder[self.preorder_index])
			self.preorder_index += 1
			index = low
			while index <= high:
				if inorder[index] == cur_root.val:
					break
				index += 1
			cur_root.left = self._building(preorder, inorder, low, index-1)
			cur_root.right = self._building(preorder, inorder, index+1, high)
			self.root = cur_root
			return self.root

	# Level wise printing nodes
	def inorder_traversal(self, cur_node):
		"""
		This will perform inorder traversal of the binary tree.

		:param cur_node: current node in the binary tree
		"""

		if not cur_node:
			return

		self.inorder_traversal(cur_node.left)
		print(cur_node.val, end=" ")
		self.inorder_traversal(cur_node.right)

if __name__ == "__main__":
	preorder = [1, 2, 4, 3, 5, 7, 8, 6]
	inorder = [4, 2, 1, 7, 5, 8, 3, 6]
	binary_tree = ConstructBT()
	binary_tree.construct_tree(preorder, inorder)
	binary_tree.inorder_traversal(binary_tree.root)
	print()