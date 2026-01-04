# --------------------
# SONAR'S EDGE
# --------------------

# Module imports
import core_classes as cc

maze1 = cc.Maze()
maze1.generate_maze("maze1", 129, 73)
#maze1.terminal_output()

game1 = cc.Game(maze1)
game1.run()
