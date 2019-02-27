'''
Robot in a Grid: Imagine a robot sitting on the upper left corner of grid with r rows and c columns. The robot can only move in two directions, right and down, but certain cells are "off limits" such that the robot cannot step on them. Design an algorithm to find a path for the robot from the top left to the bottom right.
'''

from collections import deque
from copy import deepcopy

def findPathIter(rows, cols):
    closed = []
    fringe = deque()
    start = (1,1,[])
    fringe.append(start)
    while(len(fringe) != 0):
        row, col, path = fringe.popleft()
        if row == rows and col == cols:
            return path
        closed.append((row,col))
        if (row+1,col) not in closed:
            new_path = deepcopy(path)
            new_path.append('down')
            child = (row+1,col,new_path)
            fringe.append(child)
        if (row,col+1) not in closed:
            new_path = deepcopy(path)
            new_path.append('right')
            child = (row,col+1,new_path)
            fringe.append(child)
    return []

def findPathRecur(curRow, curCol, rows, cols, closed, path):
    if curRow == rows and curCol == cols:
        return path
    else:
        closed.append((curRow,curCol))
        if curRow+1 <= rows and (curRow+1,curCol) not in closed:
           new_path = deepcopy(path)
           new_path.append('down')
           return findPathRecur(curRow+1, curCol, rows, cols, closed, new_path)
        if curCol+1 <= cols and (curRow,curCol+1) not in closed:
           new_path = deepcopy(path)
           new_path.append('right')
           return findPathRecur(curRow, curCol+1, rows, cols, closed, new_path)

def howManyPathsIter(rows, cols):
    paths = {}
    for r in range(rows):
        for c in range(cols):
            if r==0 and c==0:
                paths[(0,0)] = 1
            else:
                paths[(r,c)] = 0
                if r-1 >= 0:
                    paths[(r,c)] = paths[(r,c)] + paths[(r-1,c)]
                if c-1 >= 0:
                    paths[(r,c)] = paths[(r,c)] + paths[(r,c-1)]
    return paths[(rows-1,cols-1)]  

def howManyPathsRecur(curRow, curCol, visited):
    if curRow == 1 and curCol == 1:
        return 1
    else:
        if (curRow,curCol) in visited:
            return visited[(curRow,curCol)]
        left = 0
        up = 0
        if curRow-1 >=1:
            if (curRow-1,curCol) not in visited:
                left =  howManyPathsRecur(curRow-1, curCol, visited)
            else:
                left = visited[(curRow-1, curCol)]
        if curCol-1 >=1:
            if (curRow,curCol-1) not in visited:
                up =  howManyPathsRecur(curRow, curCol-1, visited)
            else:
                up = visited[(curRow, curCol-1)]
        total = up + left
        visited[(curRow,curCol)] = total
        return total

def main():
    rows = int(input("Enter no of rows"))
    cols = int(input("Enter no of columns"))
    print("Enter 1 to find a path iteratively or 2 for recursively, 3 for finding no of paths iteratively or 4 for recursively and 5 to exit")
    while(True):
        choice = input("Enter your choice")
        if choice == "1":
            path = findPathIter(rows, cols)
            print(path)
        elif choice == "2":
            path = findPathRecur(1, 1, rows, cols, [], [])
            print(path)
        elif choice == "3":
            paths = howManyPathsIter(rows, cols)
            print(paths)
        elif choice == "4":
            paths = howManyPathsRecur(rows, cols, {})
            print(paths)
        elif choice == "5":
            return

if __name__ == "__main__":
    main()
