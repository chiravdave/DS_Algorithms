'''
construct_tree(): creates a binary search tree.
ShowTree(): Prints nodes level by level.
checkBalanced(): Checks if the tree is balanced or not. A balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one
checkBST(): Checks if a tree is a valid binary search tree or not
'''

from typing import List

class Node:

	def __init__(self, val: int):
		self.val = val
		self.left = None
		self.right = None

class BST:

	def __init__(self):
		self.root = None

	def construct_tree(self, values: List[int]) -> None:
		"""
		This method will construct a BST from the list of input values.

		:param values: list of values to use for constructing BST
		"""

		for value in values:
			if(self.root == None):
				self.root = Node(value)
			else:
				temp = self.root
				while(True):
					if(value <= temp.val):
						if(temp.left == None):
							temp.left = Node(value)
							break
						else:
							temp = temp.left
					else:
						if(temp.right == None):
							temp.right = Node(value)
							break
						else:
							temp = temp.right

	def show_tree(self) -> None:
		"""
		This method will print level-wise nodes.
		"""

		node_list = []
		self._get_nodes_by_level(self.root, node_list, 0)
		height = len(node_list)
		for i in range(height):
			print("Nodes at level {} are:".format(i))
			for value in node_list[i]:
				print(value),
			print

	def _get_nodes_by_level(self, cur_node: Node, node_list: List[Node], depth: int) -> None:
		"""
		This method will store nodes level-wise.

		:param cur_node: current node under examination
		:param node_list: list to store nodes level-wise
		:param depth: current dept into consideration
		"""

		if(cur_node != None):
			if(len(node_list) == depth):
				new_list = []
				new_list.append(cur_node.val)
				node_list.append(new_list)
				self._get_nodes_by_level(cur_node.left, node_list, depth+1)
				self._get_nodes_by_level(cur_node.right, node_list, depth+1)
			else:
				node_list[depth].append(cur_node.val)
				self._get_nodes_by_level(cur_node.left, node_list, depth+1)
				self._get_nodes_by_level(cur_node.right, node_list, depth+1)

	def check_balanced(self) -> None:
		"""
		This method will check if the tree is balanced or not.
		"""

		flag = self._balance_helper(self.root)
		if (flag == -1):
			print("Not balanced")
		else:
			print("Balanced")

	def _balance_helper(self, cur_node: Node) -> int:
		"""
		This method will recursively check if the tree is balanced or not.

		:param cur_node: current node under consideration
		:rtype: if the tree is balanced or not
		"""

		if not cur_node:
			return 0

		else:
			# Checking if left subtree is balanced or not
			height_left = self._balance_helper(cur_node.left)
			# If the left subtree is not balanced then no need to check further
			if(height_left == -1):
				return height_left
			# Checking if right subtree is balanced or not
			height_right = self._balance_helper(cur_node.right)
			# If the right subtree is not balanced then no need to check further
			if(height_right == -1):
				return height_right
			# Checking if the tree under the current node is balanced or not
			if(abs(height_left - height_right) > 1):
				return -1
			else:
				return max(height_left, height_right) + 1

	def check_BST(self) -> None:
		"""
		This method will check if the tree is a BST or not.
		"""

		flag = self._check_helper(self.root, None, None)
		if flag:
			print("BST")
		else:
			print("Not a BST")

	def _check_helper(self, cur_node: Node, minimum: int, maximum: int) -> bool:
		"""
		This method will recursively check if the tree is a BST or not.

		:param cur_node: current node under consideration
		:param minimum: minimum value for the current node
		:param maximum: maximum value for the current node
		:rtype: if the tree under the current node is a BST or not
		"""

		if not cur_node:
			return True
		else:
			if (minimum and cur_node.val <= minimum) or (maximum and cur_node.val > maximum):
				return False
			return self._check_helper(cur_node.left, minimum, cur_node.val) and self._check_helper(cur_node.right, cur_node.val, maximum)

def main():
	tree = BST()
	tree.construct_tree([3,2,1,4,5])
	tree.show_tree()
	tree.check_balanced()
	tree.check_BST()

if __name__ == '__main__':
	main()