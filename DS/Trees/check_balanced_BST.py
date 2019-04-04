'''
construct_tree(): creates a binary search tree.
ShowTree(): Prints nodes level by level.
checkBalanced(): Checks if the tree is balanced or not. A balanced tree is defined to be a tree such that the heights of the two subtrees of any node never differ by more than one
checkBST(): Checks if a tree is a valid binary search tree or not
'''

class Node:

	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class BST:

	def __init__(self):
		self.root = None

	def construct_tree(self, values):
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

	#Level wise printing nodes
	def show_tree(self):
		node_list = []
		self.get_nodes_by_level(self.root, node_list, 0)
		height = len(node_list)
		for i in range(height):
			print("Nodes at level {} are:".format(i))
			for value in node_list[i]:
				print(value),
			print

	#Level wise storing nodes
	def get_nodes_by_level(self, temp, node_list, depth):
		if(temp != None):
			if(len(node_list) == depth):
				new_list = []
				new_list.append(temp.val)
				node_list.append(new_list)
				self.get_nodes_by_level(temp.left, node_list, depth+1)
				self.get_nodes_by_level(temp.right, node_list, depth+1)
			else:
				node_list[depth].append(temp.val)
				self.get_nodes_by_level(temp.left, node_list, depth+1)
				self.get_nodes_by_level(temp.right, node_list, depth+1)

	#Checks if the tree is balanced or not
	def check_balanced(self):
		flag = self.balance_helper(self.root)
		if (flag == -1):
			print("Not balanced")
		else:
			print("Balanced")

	def balance_helper(self, temp):
		if(temp == None):
			return 0
		else:
			height_left = self.helper(temp.left)
			if(height_left == -1):
				return height_left
			height_right = self.helper(temp.right)
			if(height_right == -1):
				return height_right
			if(abs(height_left - height_right) > 1):
				return -1
			else:
				return max(height_left, height_right) + 1

	def check_BST(self):
		flag = self.check_helper(self.root, None, None)
		if(flag == -1):
			print("Not a BST")
		else:
			print("BST")

	def check_helper(self, temp, minimum, maximum):
		if(temp == None):
			return 1
		else:
			if((minimum != None and temp.val <= minimum) or (maximum != None and temp.val > maximum)):
				return -1
			if (self.check_helper(temp.left, minimum, temp.val) == -1 or self.check_helper(temp.right, temp.val, maximum) == -1):
				return -1
			return 1

def main():
	tree = BST()
	tree.construct_tree([3,2,1,4,5])
	#tree.show_tree()
	#tree.check_balanced()
	tree.check_BST()

if __name__ == '__main__':
	main()