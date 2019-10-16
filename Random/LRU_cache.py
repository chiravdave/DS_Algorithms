"""
Implement an LRU (Least Recently Used) cache. It should be able to be initialized with a cache size n, 
and contain the following methods:

1) set(key, value): sets key to value. If the cache is full then we add a new item, and remove the least 
					recently used item.
2) get(key): gets the value at key. If no such key exists, return null.

Each operation should run in O(1) time.
"""

from typing import Optional

class LRU:

	def __init__(self, capacity: int):
		self.capacity = capacity
		self.count = 0
		self.mapping = dict()
		self.front = None
		self.rear = None

	class Node:

		def __init__(self, key: int, value: int):
			self.key = key
			self.value = value
			self.next = None
			self.prev = None

	def _add_to_front(self, key: int, value: int) -> None:
		"""
		This method will add the key, value pair at the front of the queue.

		:param key: input key
		:param value: input value
		"""

		new_node = self.Node(key, value)
		new_node.next = self.front
		self.front.prev = new_node
		self.front = new_node
		self.mapping[key] = new_node

	def _update(self, key: int, value: int) -> None:
		"""
		This method will update the key with the new value and will move this pair at the front.

		:param key: old key
		:param value: new value
		"""

		node = self.mapping[key]
		node.value = value

		# Checking if the updated node is not already at the front
		if node.prev:
			# Updating the previous node's next link
			node.prev.next = node.next

			# Checking if updated node is not the last node in the queue
			if node.next:
				# Updating the next node's previous link
				node.next.prev = node.prev

			# Updating link for the rear node
			else:
				self.rear = self.rear.prev

			# Moving the updated node at the front
			node.prev = None
			self.front.prev = node
			node.next = self.front
			self.front = node

	def set(self, key: int, value: int) -> None:
		"""
		This method will add or update memory the input key, value pair. If the cache is full
		then it will remove the least recently used item from the memory.

		:param key: input key
		:param value: input value
		"""

		if not self.front:
			self.front = self.Node(key, value)
			self.rear = self.front
			self.count += 1
			self.mapping[key] = self.front

		else:
			# Checking if the key is already present
			if key in self.mapping:
				# Updating key, value pair
				self._update(key, value)

			# Checking if memory is not full
			elif self.count < self.capacity:
				# Adding the new key, value pair at the front
				self._add_to_front(key, value)
				self.count += 1

			# Memory is full
			else:
				# Adding the new key, value pair at the front
				self._add_to_front(key, value)
				# Removing the least recently used item from the rear end
				self.mapping.pop(self.rear.key)
				self.rear = self.rear.prev
				self.rear.next = None

	def get(self, key: int) -> Optional[int]:
		"""
		It will return the value of the input key if present.

		:param key: input key
		:rtype: value corresponding to the input key
		"""

		if key in self.mapping:
			return self.mapping[key].value

		else:
			return None

	def show_memory(self) -> None:
		"""
		This method will print the key, value pair in the order of most recently used to least
		recently used items.
		"""

		node = self.front
		while node:
			print(node.key, node.value)
			node = node.next

if __name__ == "__main__":
	cache = LRU(3)
	print("Enter 1 to add/update pair\nEnter 2 to get value of a key\nEnter 3 to see the memory\
		\nEnter 4 to exit")
	while True:
		ch = int(input("Enter your choice: "))
		if ch == 1:
			key, value = map(int, (input("Enter the key and value: ").split()))
			cache.set(key, value)

		elif ch == 2:
			key = int(input("Enter the key to look for: "))
			print("Value corresponding to the key {} is: {}".format(key, cache.get(key)))

		elif ch == 3:
			cache.show_memory()

		elif ch == 4:
			exit()

		else:
			print("Wrong choice!")