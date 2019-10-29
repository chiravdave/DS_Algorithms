'''
WAP to perform the following tasks on a Binary Search Tree:
1) Find in-order successor.
2) Find first common ancester.
'''

from typing import Optional

class Node:

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BST:

	def __init__(self, root):
		self.root = root

	def _search_leftmost_rightsubtree(self, cur_node: Node) -> int:
		"""
		This method will search the left most node under the current node.

		:param cur_node: current node under consideration
		:rtype: left most node as in-order successor
		"""

		if not cur_node.left:
			return cur_node.val
		else:
			return self._search_leftmost_rightsubtree(cur_node.left)

	def _helper_inorder_successor(self, val: int, cur_node: Optional[Node], successor: Optional[Node]) -> Optional[int]:
		"""
		This method will find the in-order successor for the current node.

		:param val: node's value whose in-order successor we want to find
		:param cur_node: current node under consideration
		:param successor: successor of the current node under consideration
		:rtype: in-order successor of the current node
		"""

		if not cur_node:
			return None

		elif cur_node.val == val:
			# Search leftmost node in the right sub tree if present
			if cur_node.right:
				return self._search_leftmost_rightsubtree(cur_node.right)
			# Checking if a successor exists
			elif successor:
				return successor.val
			# No in-order successor
			else:
				return None

		elif cur_node.val > val:
			return self._helper_inorder_successor(val, cur_node.left, cur_node)
		else:
			return self._helper_inorder_successor(val, cur_node.right, successor)

	def get_inorder_successor(self, val: int) -> Optional[int]:
		return self._helper_inorder_successor(val, self.root, None)

	def _helper_first_common_ancester(self, cur_node, low_val, high_val):
		if not cur_node:
			return None
		# Ancester's value will be in between the two nodes
		elif cur_node.val in range(low_val, high_val+1):
			return cur_node.val
		elif low_val > cur_node.val:
			return self._helper_first_common_ancester(cur_node.right, low_val, high_val)
		else:
			return self._helper_first_common_ancester(cur_node.left, low_val, high_val)

	def get_first_common_ancester(self, val_1: int, val_2: int):
		if val_1 <= val_2:
			return self._helper_first_common_ancester(self.root, val_1, val_2)
		else:
			return self._helper_first_common_ancester(self.root, val_2, val_1)

def main():
	root = Node(20)
	root.left, root.right = Node(8), Node(22)
	root.left.right = Node(12)
	root.left.left = Node(4)
	root.left.right.left = Node(10)
	root.left.right.right = Node(14)
	tree = BST(root)
	print('The inorder successor of {} is: {}'.format(22, tree.get_inorder_successor(22)))
	print('The first common ancestor of {} and {} is: {}'.format(10, 22, tree.get_first_common_ancester(10, 22)))

if __name__ == "__main__":
	main()