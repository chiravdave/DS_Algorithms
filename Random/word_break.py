"""
Given a non-empty string s and a dictionary containing a list of non-empty words, add spaces in s to construct
a sentence where each word is a valid dictionary word. Return all such possible sentences.

Input:
	s = "catsanddog"
	wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
	[
  		"cats and dog",
  		"cat sand dog"
	]
"""

from typing import List

class Trie:

	def __init__(self):
		self.root = self.Node()


	class Node:
		"""
		Class to represent a node inside a trie. 
		"""

		def __init__(self):
			self.children = {}
			self.is_end_of_word = False

	def build(self, word_dict: dict) -> None:
		"""
		This method will add all the dictionary words inside a Trie.

		:param root: root node of the Trie
		"""

		for word in word_dict:
			self._add_word(word)

	def _add_word(self, word: str) -> None:
		"""
		This helper method will add a word inside the Trie.

		:param cur_node: current node under examination
		"""

		cur_node = self.root

		for ch in word:
			if ch not in cur_node.children:
				cur_node.children[ch] = self.Node()
			cur_node = cur_node.children[ch]

		cur_node.is_end_of_word = True

	def is_valid_word(self, word) -> bool:
		"""
		This method is just for sanity checking.

		:param word: word to test
		:rtype: true if the word is present else false
		"""

		cur_node = self.root
		for ch in word:
			if ch not in cur_node.children:
				break
			else:
				cur_node = cur_node.children[ch]

		if cur_node.is_end_of_word:
			return True

		else:
			return False

def get_possible_sentences(s: str, word_dict: List[str]) -> List[str]:
	"""
	This function will return all possible valid sentences.

	:param s: input string
	:param word_dict: list of dictionary words
	:rtype: list of valid sentences
	"""

	trie = Trie()
	trie.build(word_dict)
	possible_sentences = []
	helper(s, 0, trie.root, [], possible_sentences)
	return possible_sentences

def helper(s: str, cur_index: int, root, cur_str: List[str], possible_sentences: List[str]) -> None:
	"""
	This function will break the input message into valid tokens.

	:param s: input string
	:param cur_index: index of a character in the input string under examination
	:param root: root node of the trie
	:param cur_str: list to store words of a valid sentence found till now
	:possible_sentences: list to store all valid sentences
	"""

	cur_node = root
	n_chars = len(s)
	start = cur_index
	while start < n_chars:
		if s[start] in cur_node.children:
			cur_node = cur_node.children[s[start]]
			# If this is an end of a word then will move to look for the next valid word
			if cur_node.is_end_of_word:
				cur_str.append(s[cur_index:start+1])
				helper(s, start+1, root, cur_str, possible_sentences)
				cur_str.pop()
			start += 1
		# If we cannot find a word then there is no point of going further
		else:
			return

	# Checking if we have considered all the characters
	if cur_index == n_chars:
		possible_sentences.append(' '.join(cur_str))


if __name__ == "__main__":
	s = "catsandog"
	word_dict = ["cats", "dog", "sand", "and", "cat"]
	print("Possible Sentences are:")
	print(get_possible_sentences(s, word_dict))
