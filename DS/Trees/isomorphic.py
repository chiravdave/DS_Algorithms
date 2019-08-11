class Tree:

	class Node:

		def __init__(self, data):
			self.val = data
			self.left = None
			self.right = None

	def __init__(self):
		self.root = None

def check_isomorphic(root_A, root_B) -> bool:
	# Check if both the nodes are null
	if root_A == root_B == None:
		return True
	# Check if one of the node is null and the other is not
	elif (root_A == None and root_B != None) or (root_B == None and root_A != None):
		return False
	# Check if the value at both the nodes are equal or not
	elif root_A.val != root_B.val:
		return False
	# Check if the children are also isomorphic
	else:
		return (check_isomorphic(root_A.left, root_B.left) and check_isomorphic(root_A.right, root_B.right)) or \
				(check_isomorphic(root_A.left, root_B.right) and check_isomorphic(root_A.right, root_B.left))

if __name__ == "__main__":
	tree_A = Tree()
	tree_A.root = tree_A.Node(1)
	tree_A.root.left = tree_A.Node(2)
	tree_A.root.right = tree_A.Node(3)
	tree_A.root.left.left = tree_A.Node(4)
	tree_A.root.left.right = tree_A.Node(5)
	tree_A.root.right.left = tree_A.Node(6)
	tree_A.root.left.right.left = tree_A.Node(7)
	tree_A.root.left.right.right = tree_A.Node(8)

	tree_B = Tree()
	tree_B.root = tree_A.Node(1)
	tree_B.root.left = tree_A.Node(3)
	tree_B.root.right = tree_A.Node(2)
	tree_B.root.right.left = tree_A.Node(4)
	tree_B.root.right.right = tree_A.Node(5)
	tree_B.root.left.right = tree_A.Node(6)
	tree_B.root.right.right.left = tree_A.Node(8)
	tree_B.root.right.right.right = tree_A.Node(7)

	print(check_isomorphic(tree_A.root, tree_B.root))