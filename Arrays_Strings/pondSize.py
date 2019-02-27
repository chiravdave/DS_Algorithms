''' 
Pond Sizes: You have an integer matrix representing a plot of land, where the value at that location represents the height above sea level. A value of zero indicates water. 
            A pond is a region of water connected vertically, horizontally, or diagonally. The size of the pond is the total number of connected water cells. Write a method 
            to compute the sizes of all ponds in the matrix.
Input:
      0 2 1 0
      0 1 0 1
      1 1 0 1
      0 1 0 1      
Output: 2, 4, 1 (in any order)
'''
from collections import deque

def getPondDepth(a, row, col, rows, cols):
    depth = 1
    queue = deque()
    queue.append((row, col))
    a[row][col] = -1
    while(len(queue) > 0):
        row, col = queue.pop()
        if(row>0 and col>0 and (a[row-1][col-1] == 0)):
            a[row-1][col-1] = -1
            depth = depth + 1
            queue.append((row-1, col-1))
        if(row>0 and (a[row-1][col] == 0)):
            a[row-1][col] = -1
            depth = depth + 1
            queue.append((row-1, col))
        if(row<0 and (col+1)<cols and (a[row-1][col+1] == 0)):
            a[row-1][col+1] = -1
            depth = depth + 1
            queue.append((row-1, col+1))
        if(col>0 and (a[row][col-1] == 0)):
            a[row][col-1] = -1
            depth = depth + 1
            queue.append((row, col-1))
        if((col+1)<cols and (a[row][col+1] == 0)):
            a[row][col+1] = -1
            depth = depth + 1
            queue.append((row, col+1))
        if((row+1)<rows and col>0 and (a[row+1][col-1] == 0)):
            a[row+1][col-1] = -1
            depth = depth + 1
            queue.append((row+1, col-1))
        if((row+1)<rows and (a[row+1][col] == 0)):
            a[row+1][col] = -1
            depth = depth + 1
            queue.append((row+1, col))
        if((row+1)<rows and (col+1)<cols and (a[row+1][col+1] == 0)):
            a[row+1][col+1] = -1
            depth = depth + 1
            queue.append((row+1, col+1))
    return depth

def pondSizes(a):
    sizes = set()
    rows = len(a)
    cols = len(a[0])
    for i in range(rows):
        for j in range(cols):
            if(a[i][j] == 0):
                sizes.add(getPondDepth(a, i, j, rows, cols))
    return sizes
    
if __name__ == '__main__':
    print('The pool sizes are : {}'.format(pondSizes([[0,2,1,0],[0,1,0,1],[1,1,0,1],[0,1,0,1]])))
