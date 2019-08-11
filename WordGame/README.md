# Table of Contents
1. [Problem Statement](README.md#problem-statement)
2. [Dependencies](README.md#dependencies)
3. [Solution Explanation](README.md#solution-explanation)
4. [Project Structure](README.md#project-structure)
5. [I/O Format](README.md#io-format)
6. [Instructions to run the code](README.md#instructions-to-run-the-code)
7. [Performance](README.md#performance)

# Problem Statement 
Given a MXN board where every cell has one character, find words that can be formed by a sequence of adjacent (top, bottom, left, right, diagonal) letters. Words must be 3 or more letters and we may move to any of the 8 adjacent letters, however, a word should not have multiple instances of the same cell. In order to check if a string is a valid word, we can implement a naive dictionary solution for simplicity. 

# Dependencies
* [Python3](https://www.python.org/downloads/)

# Solution Explanation
If we need to find all possible valid words that can be formed by traversing the board, it is very important to consider every character as a starting character and from there onwards find all possible words starting with it. This can be easily achieved by simply going through every character starting from the top left corner and going till the bottom right corner. And, while we are traversing through the board we can keep track of visited cells to make sure that we don't consider a cell more than once. But this approach is like searching in the wild, similar to uninformed search. However, we can do actually do better than this by simply utilizing some information that is given to us.

Since, we are already given a collection of valid words, we can use it to extract information and use it for searching. We can implement a [Trie](https://en.wikipedia.org/wiki/Trie) data structure to store the collection of valid words. A Trie, also known as a prefix tree, is an efficient way to store and retrieve information. Once we are done creating our prefix tree, we can traverse the board in search of valid words only when the sequence of characters found are present in our prefix tree.

# Project Structure
    WordGame
    ├── data                     # Input/Output folder
    │    ├── sample1             # Sample 1 folder
    │    │   ├── board.txt       # Input file for the 2D board
    │    │   ├── dictionary.txt  # Input file for the dictionary words
    ├── src                      # Source folder
    │    ├── valid_words.py      # Main script to run
    ├── tests                    # Unit test folder
    │    ├── case1               # Test case 1
    │    │   ├── board.txt       # Input file for the 2D board
    │    │   ├── dictionary.txt  # Input file for the dictionary words
    │    ├── ...
    │    ├── test1.py            # Test script    
    ├── README.md                # Readme file
    
# I/O Format
Both the board information and the list of dictionary words needs to be in a **.txt** file. All the valid words found inside the board will be written out to an **output.txt** file and will be saved inside the same directory where the input files are.
   
   * Text file for the board:
        * Every row needs to be present in a separate line and the characters inside the row needs to be separated by a comma. E.x:
         
               Line1: R,A,E,L              
               Line2: M,O,F,S
               Line3: T,E,O,K
               Line4: N,A,T,I
               
   * Text file for the list of dictionary words:
        * Every word needs to be present in a separate line. E.x:
               
               Line1: TEA
               Line2: TIK
               Line3: FOE
               Line4: MEAT
               
**NOTE:** You can look inside the **data** folder to understand how to prepare these files.

# Instructions to run the code
Step 1. Install all the [dependencies](README.md#dependencies).

Step 2. Create a folder and prepare the input files as mentioned in [I/O Format](README.md#io-format) section.

Step 3. Go inside the **src** folder and run this command **python3 valid_words.py [board_file_loc] [dictionary_file_loc]**. The first argument is the 			complete path to the file containing the board information and the second argument is the complete path to the file containing the list of dictionary words.

# Performance
   * This script finds **457** valid words inside a **15X16** board and using a list of **84K** dictionary words in 0.85 secs (see sample3).
   * This script finds **2643** valid words inside a **18X18** board and using a list of **84K** dictionary words in 1 sec (see sample4).
   