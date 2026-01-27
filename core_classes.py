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

class Player(pygame.sprite.Sprite):
    
    # Initialise attributes.
    def __init__(self, pos, tile_size, screen_pos=[640,360], inventory=[], keybinds={}, echo_cool=0, speed_buff=False, health=10, max_health=10, speed=5):
        super().__init__()
        self.image = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (32, 144, 255), (tile_size//2, tile_size//2), tile_size//2)
        self.rect = self.image.get_rect(topleft=(pos[0], pos[1]))

        self.pos = pos
        self.screen_pos = screen_pos        
        self.direction = {
            "u": False,
            "d": False,
            "l": False,
            "r": False
        }
        self.inventory = inventory
        self.keybinds = keybinds
        self.echo_cool = echo_cool
        self.speed_buff = speed_buff
        self.health = health
        self.max_health = max_health
        self.speed = speed
    
    # Echolocation
    def echolocation(self): # Will add attributes in a future sprint
        # Reveal tiles ahead
        self.echo_cool = 20
    
    # Move the player
    def move_player(self):

        dx = dy = 0
        
        # Update player position
        if self.direction["u"]:
            dy = -self.speed
        if self.direction["d"]:
            dy = self.speed
        if self.direction["l"]:
            dx = -self.speed
        if self.direction["r"]:
            dx = self.speed
        
        # Clear differences if conflicts
        if self.direction["u"] and self.direction["d"]:
            dy = 0
        if self.direction["r"] and self.direction["l"]:
            dx = 0
        
        self.pos[0] += dx
        self.pos[1] += dy
        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]

#####################

# Enemy class
# Types of enemy will inherit from this base class if they have special abilities, which I may implement near the end of development if I have time.

class Enemy(pygame.sprite.Sprite):

    # Initialise attributes.
    def __init__(self, pos, tile_size, attack=2, speed=2, sense_strength=(0.1,0.1), loot=[]):
        super().__init__()
        self.pos = pos
        self.attack = attack
        self.speed = speed
        self.sense_strength = sense_strength
        self.loot = loot
        self.path = []

        self.image = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (tile_size//2, tile_size//2), tile_size//2)
        self.rect = self.image.get_rect(topleft=(int(pos[0]), int(pos[1])))
    
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

class Chest(pygame.sprite.Sprite):

    # Initialise object
    def __init__(self, pos, tile_size, loot=[]):
        super().__init__()
        self.loot = loot
        self.pos = pos

        self.image = pygame.Surface((tile_size, tile_size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 0), (tile_size//2, tile_size//2), tile_size//2)
        self.rect = self.image.get_rect(topleft=(self.pos[0], self.pos[1]))

    # Open chest
    def open_chest(self):
        # Drop all items at the current tile
        # Despawn
        pass

#####################

# Tile class

class Wall(pygame.sprite.Sprite):

    # Iniitalise object with parent object's attributes and methods alongside a boolean for being a wall or path.
    def __init__(self, row, col, tile_size):

        super().__init__()
        self.row = row
        self.col = col
        self.image = pygame.Surface((tile_size, tile_size))
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect(topleft=(int(col)*tile_size, int(row)*tile_size))

#####################

# Game class

class Game:

    # Initialise object.
    def __init__(self, maze, scale=2, window_width=1280, window_height=720):
        
        self.maze = maze.maze
        self.scale = scale
        self.running = True
        pygame.init()
        self.clock = pygame.time.Clock()
        self.tile_size = 20
        
        self.walls = pygame.sprite.Group()
        self.chests = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        
        # Give the window the name "Sonar's Edge".
        pygame.display.set_caption("Sonar's Edge")

        self.spawn_enemies(100)
        self.spawn_chests(50)
        
        self.screen = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN|pygame.SCALED)


    # Handle running the game
    def run(self):
        
        # Make game run at 60fps
        tick = self.clock.tick(60) / 1000
        self.player = Player([1,1], tile_size=self.tile_size, speed=0.5)

        # Add tiles to the tile list
        y = 0
        for row in self.maze:
            x = 0

            for col in self.maze[row]:
                cell = self.maze[row][col]

                if cell["wall"]:
                    self.walls.add(Wall(row, col, self.tile_size*self.scale))

                x += self.tile_size

            y += self.tile_size
        
        # Run the game
        while self.running:            
    
            # Draw the maze
            self.draw_maze()
 
            # Process pygame events
            for event in pygame.event.get():

                # Quit if the user wants to quit
                if event.type == pygame.QUIT:
                    self.running = False
                
                # Process key presses. Will implement keybinds later. For now, just WASD.
                if event.type == pygame.KEYDOWN:

                    # W
                    if event.key == pygame.K_w:
                        self.player.direction["u"] = True
                    # A
                    if event.key == pygame.K_a:
                        self.player.direction["l"] = True                    
                    # S
                    if event.key == pygame.K_s:
                        self.player.direction["d"] = True                    
                    # D
                    if event.key == pygame.K_d:
                        self.player.direction["r"] = True
                
                # Process key lifts. Will implement keybinds later. For now, just WASD.
                if event.type == pygame.KEYUP:

                    # W
                    if event.key == pygame.K_w:
                        self.player.direction["u"] = False
                    # A
                    if event.key == pygame.K_a:
                        self.player.direction["l"] = False                    
                    # S
                    if event.key == pygame.K_s:
                        self.player.direction["d"] = False                    
                    # D
                    if event.key == pygame.K_d:
                        self.player.direction["r"] = False
            
            # Update screen
            pygame.display.flip()
            
            # Handle player movement
            self.player.move_player()
    
    # Draw the maze
    def draw_maze(self):

        # Give the screen a grey background
        self.screen.fill((75, 75, 75))

        # Draw walls, chests and enemies
        self.walls.draw(self.screen)
        self.chests.draw(self.screen)
        self.enemies.draw(self.screen)

        # Draw the player
        self.screen.blit(self.player.image, self.player.rect)

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
                x, y = int(column)*self.tile_size*self.scale + self.tile_size*self.scale//4, int(row)*self.tile_size*self.scale + self.tile_size*self.scale//4
                self.enemies.add(Enemy(tile_size=self.tile_size, pos=[x, y]))
    
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
                x, y = int(column)*self.tile_size*self.scale + self.tile_size*self.scale//4, int(row)*self.tile_size*self.scale + self.tile_size*self.scale//4
                self.chests.add(Chest(tile_size=self.tile_size, pos=[x, y]))