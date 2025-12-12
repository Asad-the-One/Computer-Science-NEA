# --------------------
# CORE ALGORITHMS
# --------------------

# This Python file contains long functions and procedures. It is imported into "main.py".
# This is done for the sake of code maintainability.

# ##################### 

# ---------------
# Maze generation - Prim's algorithm
# ---------------

# Module imports
import random

# Function beginning
def generate_maze(num_rows, num_cols, knock_prob=0.1):

    # If num_rows or num_cols is even, make it odd.
    num_rows = (num_rows//2) * 2 + 1 + 2
    num_cols = (num_cols//2) * 2 + 1 + 2
	
    # Generate a maze where every cell is a wall
    maze = [[1 for i in range(num_cols)] for i in range(num_rows)]

    
    # Start at a random odd cell. [odd number row, odd number column] Set it to a path cell.
    start_cell = [random.randrange(0, num_rows-1, 2), random.randrange(0, num_cols-1, 2)]
    maze[start_cell[0]][start_cell[1]] = 0
    
    # Directions to navigate to frontier cells.
    directions = [(0, -2),(0, 2),(2, 0),(-2, 0)]

    # Function to add frontier walls
    def add_frontiers(maze, directions, start_cell, frontier_cells):

        # Add cells for each direction
        for direction_row, direction_col in directions:

            neighbour_row = start_cell[0] + direction_row
            neighbour_col = start_cell[1] + direction_col

            # Check bounds and ensure that selected frontiers are walls.
            if 1 <= neighbour_row < num_rows-1 and 1 <= neighbour_col < num_cols-1:

                if maze[neighbour_row][neighbour_col] == 1:

                    frontier_cells.append([neighbour_row, neighbour_col, start_cell[0], start_cell[1]])
            
        return frontier_cells

    # Create the first set of frontier cells
    frontier_cells = add_frontiers(maze, directions, start_cell, [])

    # MAIN: Maze generation begins
    done = False
    while len(frontier_cells) != 0:
        
        # Pop a random frontier.
        index = random.randrange(len(frontier_cells))
        nrow, ncol, row, col = frontier_cells.pop(index)
    
        # Process the frontier cell if it's a wall.
        if maze[nrow][ncol] == 1:

            # Carve to the frontier.
            maze[nrow][ncol] = 0
            maze[(nrow + row)//2][(ncol + col)//2] = 0

            # Add new frontier cells.
            add_frontiers(maze, directions, [nrow, ncol], frontier_cells)
    
    # Define new directions to be +-1 cell rather than +-2, as was used in generation.
    directions = [(0,-1), (0,1), (1,0), (-1,0)]

    # Requirements for breaking:
    # . Must ensure there won't be any stray walls - stray walls being walls without at least one cell NSEW.

    # Iterate through all cells in the maze.
    for col in range(0,num_cols-1):
        
        for row in range(0,num_rows-1):
            
            # Only process the cell if it is a wall
            if maze[row][col] == 1:
                
                # Check each of the cells in four directions four directions, and count how many are walls.
                walls = 0
                for direction_row, direction_col in directions:
                    
                    if maze[row+direction_row][col+direction_col] == 1:
                        
                        walls += 1
                
                # If there are 3 or 4 walls surrounding it on 4 sides, don't break the wall.
                if walls <= 2 and random.random() <= knock_prob:
                    maze[row][col] = 0

    # Polish the maze.

    # Make borders one cell thick rather than 2.
    del maze[0]
    del maze[-1]
    for i in range(len(maze)):
        del maze[i][0]
        del maze[i][-1]
    
    # Add entrances to the left and right
    for i in range(len(maze)):
        if maze[i][1] == 0 and maze[i][2] == 0:
            maze[i][0] = 0
        if maze[i][-2] == 0 and maze[i][-3] == 0:
            maze[i][-1] = 0
    for i in range(len(maze[0])):
        if maze[1][i] == 0 and maze[2][i] == 0:
            maze[0][i] = 0
        if maze[-2][i] == 0 and maze[-3][i] == 0:
            maze[-1][i] = 0


    
    return maze
