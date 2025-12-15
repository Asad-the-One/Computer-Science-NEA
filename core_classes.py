# --------------------
# CORE CLASSES
# --------------------

# This file contains the main classes for the game. This is imported into "main.py".
# This is done for the sake of maintainability.

# Module imports
import json
import core_algorithms
import os

#####################

# Maze class

class Maze:
    
    # Initialise the maze attribute.
    def __init__(self):

        self.maze = {}
    
    # Load a maze from a specified JSON
    def load_maze(self, file_name):

        with open(f"{file_name}.json", "r") as f:
            self.maze = json.load(f)

    # Generate a maze and save it.
    def generate_maze(self, file_name, num_rows, num_cols):
        
        # Generate the maze.
        maze = core_algorithms.generate_maze(num_rows, num_cols)
        
        # Convert it into JSON format.
        dict_maze = {}
        for i in range(len(maze)):
            dict_maze[str(i)] = {}
            for o in range(len(maze[i])):
                dict_maze[str(i)][str(o)] = {
                        "wall": maze[i][o],
                        "discovered": False
                        }
        
        # Make this new maze the object's maze.
        self.maze = dict_maze

        # Ensure the directory "mazes" exists for storing mazes.
        if "mazes" not in os.listdir():
            print("Directory 'mazes' does not exist. Creating...")
            os.mkdir("mazes")

        # Save the file if the "mazes" entry in the list of folder contents is a folder.
        if os.path.isdir("mazes"):
            with open(f"./mazes/{file_name}.json", "w") as f:
                json.dump(self.maze, f, indent=4)
        else:
            print("Error saving: 'mazes' is not a directory.")
            
        
