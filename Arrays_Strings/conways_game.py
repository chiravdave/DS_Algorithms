import sys
import os
import numpy as np

class ConwayGame():

    #Initializes the game with given inputs
    def __init__(self, rows=5, cols=5, gen=3, grid_init_file=None, alive_prob=0.5, modified_rule=False):
        self.gen = gen
        self.modified_rule = modified_rule
        if(grid_init_file != None):
            self.grid = np.loadtxt(grid_init_file, dtype=np.int8)
            self.rows = self.grid.shape[0]
            self.cols = self.grid.shape[1]
        else:
            self.rows = rows
            self.cols = cols
            temp = np.random.binomial(rows*cols, alive_prob, (rows,cols)) / (rows*cols)
            temp[temp>=0.5] = 1
            temp[temp<0.5] = 0
            self.grid = temp.astype(int)
            np.savetxt('initial_state.txt', self.grid, fmt='%i')

    def check_alive(self, row, col):
        #To count how many neighbour cells are alive
        alive_neighbors = 0
        
        if row>0 and col>0 and self.grid[row-1][col-1] == 1:
            alive_neighbors = alive_neighbors + 1
        if row>0 and self.grid[row-1][col] == 1:
            alive_neighbors = alive_neighbors + 1
        if row>0 and (col+1)<self.cols and self.grid[row-1][col+1] == 1:
            alive_neighbors = alive_neighbors + 1
        if col>0 and self.grid[row][col-1] == 1:
            alive_neighbors = alive_neighbors + 1
        if (col+1)<self.cols and self.grid[row][col+1] == 1:
            alive_neighbors = alive_neighbors + 1
        if (row+1)<self.rows and col>0 and self.grid[row+1][col-1] == 1:
            alive_neighbors = alive_neighbors + 1
        if (row+1)<self.rows and self.grid[row+1][col] == 1:
            alive_neighbors = alive_neighbors + 1
        if (row+1)<self.rows and (col+1)<self.cols and self.grid[row+1][col+1] == 1:
            alive_neighbors = alive_neighbors + 1
        if(modified_rule):
            alive_neighbors = alive_neighbors + 1

        #Checking if the cell is alive
        if self.grid[row][col] == 1:
            if alive_neighbors < 2:
                return False
            if alive_neighbors == 2 or alive_neighbors == 3:
                return True
            return False
        else:
            if alive_neighbors == 3:
                return True
            return False       

    #Starts the game and runs till the provided generations and 
    def start_game(self, save_gen_no=-1):
        till_gen = self.gen
        #Checking if the user has specified a particular generation to run the game till
        if(save_gen_no != -1):
            till_gen = save_gen_no
 
        #Looping through generations
        for i in range(till_gen):
            #Creating a copy to hold the next generation values
            grid_copy = np.zeros((self.rows,self.cols), dtype=np.int8)

            for row in range(self.rows):
                for col in range(self.cols):
                    is_alive = self.check_alive(row, col)
                    if is_alive:
                        grid_copy[row][col] = 1
                    else:
                        grid_copy[row][col] = 0
            self.grid = grid_copy
        np.savetxt('final_state.txt', self.grid, fmt='%i')

#For getting the index positions of the options (-d, -g and -f), if provided by the user 
def get_index_options():
    options = {'-d':-1, '-g':-1, '-f':-1, '-p':-1, '-r':1}
    l = len(sys.argv)
    for i in range(1, l):
        if sys.argv[i] in options:
            options[sys.argv[i]] = i
    return options 

if __name__ == '__main__':
    #Default values for the specifications
    rows, cols, gen, grid_init_file, alive_prob, modified_rule = 5, 5, 3, None, 0.5, False
    n_args = len(sys.argv)

    #Checking if the user asked for help option
    if(n_args>12 or (n_args == 2 and (sys.argv[1] == '-h' or sys.argv[1] == '--help'))):
        print('Options (optional) for running this program:')
        print('-d 10 10: For providing rows and columns for the grid')
        print('-g 3: For providing number of generations to run the game')
        print('-f \'initial_state.txt\': For providing input file for the initial state of the game')
        print('-p 0.3: For providing probability value for the cells to be alive in the initial state')
        print('-r True: For modifying the rule of neighbor relation')
        sys.exit()
    options = get_index_options()

    #Checking if the user selected -d option for specifying dimensions of the grid
    if(options['-d'] != -1):
        index = options['-d']
        if((index+1) >= n_args or (index+2) >= n_args or sys.argv[index+1].isdigit() == False or sys.argv[index+2].isdigit() == False):
            print('If -d option is selected then you must provide rows and columns for the grid as integers')
            sys.exit()
        else:
            rows = int(sys.argv[index+1])
            cols = int(sys.argv[index+2])
    
    #Checking if the user selected -g option for specifying number of generations
    if(options['-g'] != -1):
        index = options['-g']
        if((index+1) >= n_args or sys.argv[index+1].isdigit() == False):
            print('If -g option is selected then you must provide number of generations as integer')
            sys.exit()
        else:
            gen = int(sys.argv[index+1])
    
    #Checking if the user selected -f option for specifying initial state for the game
    if(options['-f'] != -1):
        index = options['-f']
        if((index+1) >= n_args or os.path.isfile(sys.argv[index+1]) == False):
            print('If -h option is selected then you must provide a valid input file')
            sys.exit()
        else:
            grid_init_file = sys.argv[index+1]

    #Checking if the user selected -p option for specifying probability value
    if(options['-p'] != -1):
        index = options['-f']
        if((index+1) >= n_args or sys.argv[index+1].isdigit() == False):
            print('If -h option is selected then you must provide a valid input file')
            sys.exit()
        else:
            grid_init_file = sys.argv[index+1]
    game = ConwayGame(rows, cols, gen, grid_init_file)
    game.start_game()
