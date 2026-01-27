# --------------------
# SONAR'S EDGE
# --------------------

# Module imports
import core_classes as cc

maze1 = cc.Maze()
maze1.load_maze("maze1")
#maze1.terminal_output()

game1 = cc.Game(maze1, window_width=1920, window_height=1080)
game1.run()
