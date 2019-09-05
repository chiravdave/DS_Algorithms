"""
Implementing locking in a binary tree. A binary tree node can be locked or unlocked only if all of its 
descendants or ancestors are not locked. Design a binary tree node class with the following methods:

1) is_locked: which returns whether the node is locked
2) lock: which attempts to lock the node. If it cannot be locked, then it should return false.
3) unlock: which unlocks the node. If it cannot be unlocked, then it should return false.

Each method should run in O(h), where h is the height of the tree.
"""

class BT:

	def __init__(self):
		self.root = None

	class Node:

		def __init__(self, val: int, parent = None):
			self.val = val
			self.locked = False
			self.n_locked_descendents = 0
			self.parent = parent

		def is_locked(self) -> bool:
			"""
			This method will check if the node is locked or not.
			"""

			return self.locked

		def lock(self) -> bool:
			"""
			This method will attempt to lock the node.
			"""

			# Checking if the descendents are not locked
			if self._are_descendents_unlocked():
				self.locked = True

			# Checking if ancesters are not locked
			elif self._are_ancesters_unlocked():
				self.locked = True
			
			# Checking if the locking was successful
			if self.locked:
				# Updating the ancesters about this locking
				self._update_ancester(1)

			return self.locked

		def unlock(self) -> bool:
			"""
			This method will attempt to unlock the node.
			"""

			# Checking if all the descendents are not locked
			if self._are_descendents_unlocked():
				self.locked = False
			
			# Checking if ancesters are not locked
			elif self._are_ancesters_unlocked():
				self.locked = False

			# Checking if the unlocking was successful
			if not self.locked:
				# Updating the ancesters about this unlocking
				self._update_ancester(-1)

			return not self.locked

		def _are_descendents_unlocked(self) -> bool:
			"""
			This private method will check if the descendents are not locked.
			"""

			return self.n_locked_descendents == 0

		def _are_ancesters_unlocked(self) -> bool:
			"""
			This private method will check if the ancesters are not locked
			"""

			parent = self.parent
			any_ancester_locked = False
			# Checking if all the ancestors are unlocked 
			while parent:
				# If we find that an ancester is locked then we don't need to check further up
				if parent.locked:
					any_ancester_locked = True
					break
				parent = parent.parent

			return not any_ancester_locked

		def _update_ancester(self, change: int):
			"""
			This private method will update the no. of locked descendents for the ancesters.

			:param change: value to be added to the no. of locked descendents
			"""

			parent = self.parent
			while parent:
				parent.n_locked_descendents += change
				parent = parent.parent

if __name__ == "__main__":
	tree = BT()
	mapping = dict()
	tree.root= tree.Node(1)
	mapping[1] = tree.root
	tree.root.left = tree.Node(2, tree.root)
	mapping[2] = tree.root.left
	tree.root.right = tree.Node(3, tree.root)
	mapping[3] = tree.root.right
	tree.root.left.left = tree.Node(4, tree.root.left)
	mapping[4] = tree.root.left.left 
	tree.root.right.left = tree.Node(5, tree.root.right)
	mapping[5] = tree.root.right.left 
	tree.root.right.right = tree.Node(6, tree.root.right)
	mapping[6] = tree.root.right.right 
	tree.root.right.left.left = tree.Node(7, tree.root.right.left)
	mapping[7] = tree.root.right.left.left
	tree.root.right.left.right = tree.Node(8, tree.root.right.left)
	mapping[8] = tree.root.right.left.right 
	tree.root.right.right.left = tree.Node(9, tree.root.right.right)
	mapping[9] = tree.root.right.right.left 
	tree.root.right.right.right = tree.Node(10, tree.root.right.right)
	mapping[10] = tree.root.right.right.right

	print("Enter 1 to check if a node is locked\nEnter 2 to lock a node\nEnter 3 to unlock a node\nEnter 4 to exit\n")
	while True:
		ch = int(input("Enter your choice: "))
		if ch != 4:
			val = int(input("Enter the node value to work with: "))
		if ch == 1:
			print(mapping[val].is_locked())
		elif ch == 2:
			print(mapping[val].lock())
		elif ch == 3:
			print(mapping[val].unlock())
		elif ch == 4:
			break
		else:
			print("Wrong Choice!")