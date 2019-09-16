"""
A universal/unival tree is the one where all nodes under it have the same value. Given the root
to a binary tree, count the number of unival subtrees.
"""

from typing import Tuple

class Node:
	"""
	Class to represent a node inside a binary tree. 
	"""

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class UnivalTrees:

	def count_unival_subtrees(self, root: Node) -> int:
		"""
		This method will return the total number of unival subtrees inside a given binary tree.

		:param root: root of a binary tree
		:rtype: total no. of unival subtrees
		"""

		n_unival_trees, _ = self._helper(root)
		return n_unival_trees

	def _helper(self, cur_node: Node) -> Tuple[int, bool]:
		"""
		This helper method will return no. of unival subtrees under the current node and it also
		will tell if the entire tree (including the current node) is unival or not.

		:param cur_node: current node under examination
		:rtype: total no. of unival subtrees under the current node and if the entire tree (including)
				the current node is unival or not
		"""

		# Checking if we have reached end of the tree
		if not cur_node:
			return 0, True

		# Checking for leaf node
		if not cur_node.left and not cur_node.right:
			return 1, True

		else:
			# Getting no. of unival subtrees under the left subtree
			left_n_unival_trees, is_left_subtree_unival = self._helper(cur_node.left)
			# Getting no. of unival subtrees under the right subtree
			right_n_unival_trees, is_right_subtree_unival = self._helper(cur_node.right)

			cur_n_unival_tress, is_cur_tree_unival = left_n_unival_trees+right_n_unival_trees, True
			
			# Checking if the left subtree is universal or not
			if is_left_subtree_unival:
				# Checking if the current tree (including the root) is universal or not
				if cur_node.left and cur_node.left.val == cur_node.val:
						cur_n_unival_tress += 1
			# If left subtree is not unival then even currrent tree cannot be unival
			else:
				is_cur_tree_unival = False

			# Checking if the right subtree is universal or not
			if is_right_subtree_unival:
				# Checking if the current tree (including the root) is universal or not
				if cur_node.right and cur_node.right.val == cur_node.val:
						cur_n_unival_tress += 1
			# If right subtree is not unival then even currrent tree cannot be unival
			else:
				is_cur_tree_unival = False

			return cur_n_unival_tress, is_cur_tree_unival

if __name__ == "__main__":
	root = Node(5)
	root.left = Node(1)
	root.right = Node(5)
	root.right.right = Node(5)
	root.left.left = Node(5)
	root.left.right = Node(5)

	unival_trees = UnivalTrees()
	print(unival_trees.count_unival_subtrees(root))