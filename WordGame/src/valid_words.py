from typing import List, Set, Tuple
from os.path import isfile
import argparse


class Trie:
    """
    This class is for representing a Trie data structure, commonly known as a prefix tree.
    """

    def __init__(self):
        self.root = None

    class TrieNode:
        """
        This class is for representing a node inside a Trie.
        """

        def __init__(self):
            # Character -> TrieNode
            self.children = dict()
            # To specify end of a word
            self.is_end_of_word = False

    def build_tree(self, dict_file_loc: str) -> None:
        """
        This method will fetch all the valid words from the input dictionary file and then it will build a prefix tree
        from it. It will convert all the words into uppercase so that matching can be case independent.

        :param dict_file_loc: location of the dictionary file containing words
        :return: None
        """

        with open(dict_file_loc, "r") as dict_file:
            for word in dict_file:
                # Converting into uppercase so that we can have one fixed case matching
                self.__add_word(word.strip().upper())

    def __add_word(self, word: str) -> None:
        """
        This private method will add the given word to the prefix tree.

        :param word: word to be added.
        :return: None
        """

        if not self.root:
            self.root = self.TrieNode()

        n_chars = len(word)
        cur_node = self.root
        # Will insert characters one at a time
        for index in range(n_chars):
            # Checking if the current character is already present or not
            if word[index] in cur_node.children:
                cur_node = cur_node.children[word[index]]
            else:
                new_node = self.TrieNode()
                cur_node.children[word[index]] = new_node
                cur_node = new_node

        # Making the last node as the end of word
        cur_node.is_end_of_word = True


class Board:
    """
    This class is for representing the game board.
    """

    def __init__(self):
        self.board = []

    def preprocess_row(self, row: List[str]) -> None:
        """
        This method will convert each character in the row into uppercase so that matching can be case independent and
        we will prevent considering similar words multiple times that differ only in case.

        :param row: a row of the input board
        :return: None
        """

        n_chars = len(row)
        for index in range(n_chars):
            row[index] = row[index].strip().upper()

    def gen_board(self, board_file_loc: str) -> None:
        """
        This method will generate the game board from the input file.

        :param board_file_loc: location of the file containing board description
        :return: None
        """

        with open(board_file_loc, "r") as board_file:
            # Will create one row at a time
            for line in board_file:
                row = line.strip().split(",")
                self.preprocess_row(row)
                self.board.append(row)

        # Storing the location of the parent directory so that we can save the output file inside it
        self.data_dir = board_file_loc[: board_file_loc.rfind("/")]

    def write_result(self, words_found: Set[str]) -> None:
        """
        This method will write out all valid words to an output.txt file inside the same directory where the input files
        are.

        :param words_found: collection of all the valid words found
        :return: None
        """

        with open("{}/output.txt".format(self.data_dir), "w") as output_file:
            for word in words_found:
                output_file.write(word)
                output_file.write("\n")

    def __find_valid_words(
        self,
        cur_node,
        row: int,
        col: int,
        cur_word: List[str],
        visited: Set[Tuple[int]],
        words_found: Set[str],
    ) -> None:
        """
        This private method will recursively search (DFS) for valid words inside the board.

        :param cur_node: current Trie node in consideration
        :param row: current row of the board in consideration
        :param col: current col of the board in consideration
        :param cur_word: word formed till now
        :param visited: collection of board locations already visited
        :param words_found: collection of valid words found till now
        :return: None
        """

        rows, cols = len(self.board), len(self.board[0])
        # Checking if we reached end of a valid word
        if cur_node.is_end_of_word:
            word = "".join(cur_word)
            # Adding the word to the found list only if it's length is more than 2
            if len(word) >= 3:
                words_found.add(word)

        # Checking if the top left character can be considered
        if (
            row - 1 >= 0
            and col - 1 >= 0
            and (row - 1, col - 1) not in visited
            and self.board[row - 1][col - 1] in cur_node.children
        ):
            visited.add((row - 1, col - 1))
            cur_word.append(self.board[row - 1][col - 1])
            self.__find_valid_words(
                cur_node.children[self.board[row - 1][col - 1]],
                row - 1,
                col - 1,
                cur_word,
                visited,
                words_found,
            )
            visited.remove((row - 1, col - 1))
            cur_word.pop()

        # Checking if the top character can be considered
        if (
            row - 1 >= 0
            and (row - 1, col) not in visited
            and self.board[row - 1][col] in cur_node.children
        ):
            visited.add((row - 1, col))
            cur_word.append(self.board[row - 1][col])
            self.__find_valid_words(
                cur_node.children[self.board[row - 1][col]],
                row - 1,
                col,
                cur_word,
                visited,
                words_found,
            )
            visited.remove((row - 1, col))
            cur_word.pop()

        # Checking if the top right character can be considered
        if (
            row - 1 >= 0
            and col + 1 < cols
            and (row - 1, col + 1) not in visited
            and self.board[row - 1][col + 1] in cur_node.children
        ):
            visited.add((row - 1, col + 1))
            cur_word.append(self.board[row - 1][col + 1])
            self.__find_valid_words(
                cur_node.children[self.board[row - 1][col + 1]],
                row - 1,
                col + 1,
                cur_word,
                visited,
                words_found,
            )
            visited.remove((row - 1, col + 1))
            cur_word.pop()

        # Checking if the left character can be considered
        if (
            col - 1 >= 0
            and (row, col - 1) not in visited
            and self.board[row][col - 1] in cur_node.children
        ):
            visited.add((row, col - 1))
            cur_word.append(self.board[row][col - 1])
            self.__find_valid_words(
                cur_node.children[self.board[row][col - 1]],
                row,
                col - 1,
                cur_word,
                visited,
                words_found,
            )
            visited.remove((row, col - 1))
            cur_word.pop()

        # Checking if the right character can be considered
        if (
            col + 1 < cols
            and (row, col + 1) not in visited
            and self.board[row][col + 1] in cur_node.children
        ):
            visited.add((row, col + 1))
            cur_word.append(self.board[row][col + 1])
            self.__find_valid_words(
                cur_node.children[self.board[row][col + 1]],
                row,
                col + 1,
                cur_word,
                visited,
                words_found,
            )
            visited.remove((row, col + 1))
            cur_word.pop()

        # Checking if the bottom left character can be considered
        if (
            row + 1 < rows
            and col - 1 >= 0
            and (row + 1, col - 1) not in visited
            and self.board[row + 1][col - 1] in cur_node.children
        ):
            visited.add((row + 1, col - 1))
            cur_word.append(self.board[row + 1][col - 1])
            self.__find_valid_words(
                cur_node.children[self.board[row + 1][col - 1]],
                row + 1,
                col - 1,
                cur_word,
                visited,
                words_found,
            )
            visited.remove((row + 1, col - 1))
            cur_word.pop()

        # Checking if the bottom character can be considered
        if (
            row + 1 < rows
            and (row + 1, col) not in visited
            and self.board[row + 1][col] in cur_node.children
        ):
            visited.add((row + 1, col))
            cur_word.append(self.board[row + 1][col])
            self.__find_valid_words(
                cur_node.children[self.board[row + 1][col]],
                row + 1,
                col,
                cur_word,
                visited,
                words_found,
            )
            visited.remove((row + 1, col))
            cur_word.pop()

        # Checking if the bottom right character can be considered
        if (
            row + 1 < rows
            and col + 1 < cols
            and (row + 1, col + 1) not in visited
            and self.board[row + 1][col + 1] in cur_node.children
        ):
            visited.add((row + 1, col + 1))
            cur_word.append(self.board[row + 1][col + 1])
            self.__find_valid_words(
                cur_node.children[self.board[row + 1][col + 1]],
                row + 1,
                col + 1,
                cur_word,
                visited,
                words_found,
            )
            visited.remove((row + 1, col + 1))
            cur_word.pop()

    def get_valid_words(self, root) -> None:
        """
        This method will find all valid words present inside the board. It will sequentially move across all the
        characters starting from top left corner and going till bottom right corner, so that all possible words are
        taken into consideration.

        :param root: root node of the Trie
        :return: None
        """

        rows, cols = len(self.board), len(self.board[0])
        words_found, visited, cur_word = set(), set(), list()

        # Will sequentially move across all the characters starting from top left corner to bottom right corner.
        for row in range(rows):
            for col in range(cols):
                # Will search for words only if the current character is the starting character of any valid word.
                if self.board[row][col] in root.children:
                    visited.add((row, col))
                    cur_word.append(self.board[row][col])
                    self.__find_valid_words(
                        root.children[self.board[row][col]],
                        row,
                        col,
                        cur_word,
                        visited,
                        words_found,
                    )
                    visited.remove((row, col))
                    cur_word.pop()

        self.write_result(words_found)


if __name__ == "__main__":
    about = "This script will find all valid words inside a 2D board of characters using a list of dictionary words. It " \
            "takes two input files, first containing the configuration of the board and second containing list of dictionary " \
            "words. It will store the result in an 'output.txt' file and save it under the same directory where the input " \
            "files are."
    parser = argparse.ArgumentParser(description=about)
    parser.add_argument(
        "board_file",
        help="complete path for the board file (~/WordGame/data/sample1/board.txt)",
    )
    parser.add_argument(
        "dictionary_file",
        help="complete path for the dictionary file (~/WordGame/data/sample1/dictionary.txt)",
    )

    args = parser.parse_args()
    board_file_loc = args.board_file
    dict_file_loc = args.dictionary_file

    # Checking if the user has provided correct path to the input file containing the board information
    if not isfile(board_file_loc):
        print("Please provide correct path to the file containing the board information")
        exit()

    # Checking if the user has provided correct path to the input file containing the dictionary of words
    if not isfile(dict_file_loc):
        print("Please provide correct path to the file containing the dictionary of words")
        exit()

    prefix_tree = Trie()
    prefix_tree.build_tree(dict_file_loc)
    game_board = Board()
    game_board.gen_board(board_file_loc)
    game_board.get_valid_words(prefix_tree.root)
