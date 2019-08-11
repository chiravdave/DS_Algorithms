from src.valid_words import Trie, Board

prefix_tree = Trie()
game_board = Board()


def test_board1():
    prefix_tree.build_tree("tests/case1/dictionary.txt")
    game_board.gen_board("tests/case1/board.txt")
    assert game_board.board == [
        ["R", "A", "E", "L"],
        ["M", "O", "F", "S"],
        ["T", "E", "O", "K"],
        ["N", "A", "T", "I"],
    ]

    game_board.get_valid_words(prefix_tree.root)
    with open("tests/case1/output.txt", "r") as output_file:
        words_found = set()
        for word in output_file:
            words_found.add(word.strip())

    assert words_found == {"TATI", "TEA", "TIK", "FOE", "ROOK", "MEAT"}


def test_board2():
    prefix_tree.root = None
    prefix_tree.build_tree("tests/case2/dictionary.txt")
    game_board.board = []
    game_board.gen_board("tests/case2/board.txt")
    assert game_board.board == [
        ["T", "Z", "X", "C", "D"],
        ["A", "H", "N", "Z", "K"],
        ["H", "W", "O", "I", "O"],
        ["O", "R", "N", "R", "N"],
        ["A", "B", "R", "I", "N"],
    ]

    game_board.get_valid_words(prefix_tree.root)
    with open("tests/case2/output.txt", "r") as output_file:
        words_found = set()
        for word in output_file:
            words_found.add(word.strip())

    assert words_found == {"HORN", "HORIZON", "BRINR", "BRO", "AHNZX", "NNO", "BRINRN"}


def test_board3():
    prefix_tree.root = None
    prefix_tree.build_tree("tests/case3/dictionary.txt")
    game_board.board = []
    game_board.gen_board("tests/case3/board.txt")
    assert game_board.board == [
        ["T", "H", "S", "M", "A", "L", "L", "T", "R"],
        ["E", "A", "P", "C", "R", "S", "R", "P", "S"],
        ["E", "L", "I", "C", "F", "T", "O", "S", "P"],
        ["N", "I", "H", "D", "E", "T", "S", "E", "R"],
        ["N", "B", "C", "D", "W", "U", "S", "J", "I"],
        ["Y", "M", "A", "E", "S", "Y", "C", "E", "N"],
        ["P", "I", "E", "T", "G", "N", "L", "N", "G"],
    ]

    game_board.get_valid_words(prefix_tree.root)
    with open("tests/case3/output.txt", "r") as output_file:
        words_found = set()
        for word in output_file:
            words_found.add(word.strip())

    assert words_found == {
        "TEEN",
        "SMALL",
        "PIE",
        "DEW",
        "FEW",
        "MBA",
        "FET",
        "TOSS",
        "HAP",
        "HAS",
        "HEENNY",
        "NYU",
    }
