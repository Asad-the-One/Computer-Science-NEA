# --------------------
# CORE CLASSES
# --------------------

# This file contains the main classes for the game. This is imported into "main.py".
# This is done for the sake of maintainability.

# Module imports
import json
import core_algorithms
import os
import pygame
import random

#####################

# Maze class

class Maze:
    
    # Initialise attributes.
    def __init__(self):

        self.maze = {}
    
    # Load a maze from a specified JSON
    def load_maze(self, file_name):

        with open(f"./mazes/{file_name}.json", "r") as f:
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

        with open(f"./mazes/{file_name}.json", "w") as f:
            json.dump(self.maze, f, indent=4)

    # Render the maze as 0s and spaces in the terminal.
    def terminal_output(self, walls=False):
        
        output_arr = []
        # Turn the maze dictionary into a 2D array.
        # For each row:
        for i in self.maze:
            
            # Temp variable to be appended to the output array.
            temp = []

            # For each column:
            for o in self.maze[i]:
                
                # Append 1 or 0 (wall or path) to temp.
                temp.append(self.maze[i][o]["wall"])
            
            # Append temp to the output array, then reset it to empty on the next iteration.
            output_arr.append(temp)
        
        # Iterate through the output array and print only the 0s with spaces between them.
        for i in output_arr:

            temp = str(i).replace("[", "")
            temp = temp.replace("]", "")
            temp = temp.replace(",", "")
            if walls:
                temp = temp.replace("0", " ")
            else:
                temp = temp.replace("1", " ")
            print(temp)
            
#####################

# Player class

class Player:
    
    # Initialise attributes.
    def __init__(self, pos, screen_pos, direction="u", inventory=[], keybinds={}, echo_cool=0, speed_buff=False, health=10, max_health=10, speed=5):

        self.pos = pos
        self.screen_pos = screen_pos
        self.direction = direction
        self.inventory = inventory
        self.keybinds = keybinds
        self.echo_cool = echo_cool
        self.speed_buff = speed_buff
        self.health = health
        self.max_health = max_health
        self.speed = speed

#####################

# Enemy class
# Types of enemy will inherit from this base class if they have special abilities, which I may implement near the end of development if I have time.

class Enemy:

    # Initialise attributes.
    def __init__(self, position, attack=2, speed=2, sense_strength=(0.1,0.1), loot=[]):
        self.position = position
        self.attack = attack
        self.speed = speed
        self.sense_strength = sense_strength
        self.loot = loot
        self.path = []
    
    # Deal damage
    def deal_damage(self, player):
        # if touching player
        #   reduce player.health by self.attack
        #   cooldown 1 second
        pass

    # A* pathfinding
    def astar(self, maze):
        # A* algorithm returning a path to trace back up
        pass

    # Update enemy position
    def update_position(self):
        # Use self.path and self.speed to move the enemy if necessary
        pass

#####################

# Chest class

class Chest:

    # Initialise object
    def __init__(self, loot=[]):

        self.loot = loot
        self.position = []

    # Open chest
    def open_chest(self):
        # Drop all items at the current tile
        # Despawn
        pass

#####################

# Game class

class Game:

    # Initialise object.
    def __init__(self, maze, chests=[], enemies=[], window_width=1280, window_height=720):
        
        self.maze = maze.maze
        self.enemies = enemies
        self.chests = chests
        self.running = True
        pygame.init()
        self.clock = pygame.time.Clock()
        self.spawn_enemies(100)
        self.spawn_chests(50)
        
        # Give the window the name "Sonar's Edge".
        pygame.display.set_caption("Sonar's Edge")
        
        # Create maze tile sizes based on the size of the window.
        # If height < width
        if len(maze.maze) < len(maze.maze["0"]):
            # Tile size based on width
            self.tile_size = window_width//len(maze.maze["0"])
        else:
            # Tile size based on height
            self.tile_size = window_height//len(maze.maze)
        
        self.screen = pygame.display.set_mode((len(maze.maze["0"])*self.tile_size, len(maze.maze)*self.tile_size))


    # Handle running the game
    def run(self):
        
        # Make game run at 60fps
        tick = self.clock.tick(60) / 1000
        
        
        # Run the game
        while self.running:            
    
            # Draw the maze
            self.draw_maze()
 
            # Quit if the user wants to quit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
            
            # Update screen
            pygame.display.flip()
            
            # Handle player movement
    
    # Draw the maze
    def draw_maze(self):
        self.screen.fill((75, 75, 75))
        y = 0
        for row in self.maze:
            x = 0

            for col in self.maze[row]:
                cell = self.maze[row][col]

                if cell["wall"]:
                    rect = pygame.Rect(x, y, self.tile_size, self.tile_size)
                    pygame.draw.rect(self.screen, (0, 0, 0), rect)

                x += self.tile_size

            y += self.tile_size
        
        # Add enemy tiles
        for enemy in self.enemies:

            render_row = enemy.position[0] * self.tile_size + self.tile_size//2
            render_column = enemy.position[1] * self.tile_size + self.tile_size//2
            pygame.draw.circle(self.screen, (255, 0, 0), (render_column, render_row), self.tile_size//2)
        
        # Add chest tiles
        for chest in self.chests:

            render_row = chest.position[0] * self.tile_size + self.tile_size//2
            render_column = chest.position[1] * self.tile_size + self.tile_size//2
            pygame.draw.circle(self.screen, (255, 255, 0), (render_column, render_row), self.tile_size//2)

        pygame.display.update()
    
    # Spawn enemies randomly around path cells
    def spawn_enemies(self, count):

        # Get maze dimensions
        maze_dimensions = (len(self.maze)-1, len(self.maze["0"])-1)

        # Continue spawning enemies until count is 0
        while count > 0:

            # Get a random row and column
            row = str(random.randint(0, maze_dimensions[0]))
            column = str(random.randint(0, maze_dimensions[1]))

            # Add an enemy if the cell is a path cell
            if not self.maze[row][column]["wall"]:
                count -= 1
                self.enemies.append(Enemy(position=[int(row), int(column)]))
    
    # Spawn chests randomly around path cells
    def spawn_chests(self, count):

        # Get maze dimensions
        maze_dimensions = (len(self.maze)-1, len(self.maze["0"])-1)

        # Continue spawning chests until count is 0
        while count > 0:

            # Get a random row and column
            row = str(random.randint(0, maze_dimensions[0]))
            column = str(random.randint(0, maze_dimensions[1]))

            # Add a chest if the cell is a path cell
            if not self.maze[row][column]["wall"]:
                count -= 1
                self.chests.append(Enemy(position=[int(row), int(column)]))