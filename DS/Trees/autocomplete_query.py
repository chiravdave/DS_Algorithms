"""
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings,
return all strings in the set that have s as a prefix. For example, given the query string 'de' and the set
of strings [dog, deer, deal], return [deer, deal].
"""

from typing import List

class PrefixTree:
	"""
	This class will represent a prefix tree containing words from the input set.
	"""

	def __init__(self):
		self.root = self.Node()

	class Node:
		"""
		This class will represent a node inside our prefix tree.
		"""

		def __init__(self):
			self.children = {}
			self.is_end_of_word = False

	def create_tree(self, word_set: List[str]) -> None:
		"""
		This method will add words from an input set into the preifx tree.

		:param word_set: collection of words
		"""

		for word in word_set:
			self._add_word(word)

	def _add_word(self, word: str) -> None:
		"""
		This method will add an input word into the prefix tree.

		:param word: word from the set
		"""

		cur_node = self.root
		for char in word:
			if char in cur_node.children:
				cur_node = cur_node.children[char]
			else:
				new_node = self.Node()
				cur_node.children[char] = new_node
				cur_node = new_node

		cur_node.is_end_of_word = True

	def query(self, query_str: str) -> List[str]:
		"""
		Given a query string this method will return all strings in the set that have
		the query string as a prefix.

		:param query_str: input string to quer on
		:rtype: list of all strings in the set that have the query string as a prefix.
		"""

		query_result = []
		# Will first check if the query string is at all a prefix in our set of strings
		cur_node = self.root
		cur_word = []
		for char in query_str:
			if char not in cur_node.children:
				return query_result
			cur_word.append(char)
			cur_node = cur_node.children[char]

		# Now will return all complete strings from our set of strings
		self._find_complete_words(cur_node, cur_word, query_result)

		return query_result

	def _find_complete_words(self, cur_node, cur_word: List[str], query_result: List[str]):
		"""
		This method will add all complete strings to the query result.

		:param cur_node: current node under examination
		:param cur_word: current word formed
		:param query_result: list to store all complete strings
		"""

		# Checking if we have reached end of a valid word
		if cur_node.is_end_of_word:
			query_result.append("".join(cur_word))

		# Will add all the next valid character to our current word list
		for char, next_node in cur_node.children.items():
			cur_word.append(char)
			self._find_complete_words(next_node, cur_word, query_result)
			# Will pop this charatcer as we already searched for all words containing this character
			cur_word.pop()

if __name__ == "__main__":
	prefix_tree = PrefixTree()
	prefix_tree.create_tree(["dog", "deer", "deal", "pop", "popular", "pops"])
	print(prefix_tree.query("p"))