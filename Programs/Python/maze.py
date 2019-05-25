# import os, pygame
# from pygame.locals import *
# from pygame.compat import geterror
# import time

from random import shuffle

# This game will become Role Playing Game where a person 
# walks around the maze and fights with foes. Backtracing algorithm is used
# for generating maze.

# TODO: Create the algorithm for generating maze.

# Initiall create the grid
# The form of the grid is as follows:

direction = {"N": (0,-1), "S":(0,1),"E":(1,0), "W":(-1,0)}
opposite_direction  = {"N":"S", "S":"N", "E":"W", "W":"E"}
# Firstly, make grid using list.
# height and width must be number

height_default = 5
width_default = 5

def make_maze_grid(height = height_default, width = width_default):

    grid = [[[] for _ in range(width)] for _ in range(height)]

    # Take grid as the numbers
    def generate_maze_grid(current_x=0,current_y=0):
        
        move_directions = ["N","S","E","W"]

        shuffle(move_directions)
        # print("(((STEP)))")

        for move_direction in move_directions:
            
            next_x = current_x + direction[move_direction][0]
            next_y = current_y + direction[move_direction][1]

            if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid) and grid[next_x][next_y] == []:
                grid[current_x][current_y].append(opposite_direction[move_direction])
                grid[next_x][next_y].append(move_direction)
                generate_maze_grid(next_x, next_y)
            # print(grid)

    generate_maze_grid(0,0)

    return grid

# Create maze first.
def print_maze_grid(grid):
    # Print maze based on the information on grid.

    # String used for generating maze.
    maze_str = ""

    for y in range(2 * len(grid[0]) + 1):
        for x in range(2 * len(grid) + 1):
            if x % 2 == 1 and y % 2 == 1: 
                maze_str += "#"
            else:
                maze_str += "w"
        maze_str += "\n"
    print(maze_str)


# TODO: Putting codes in the main program.
def main():
    grid = make_maze_grid()

    print(grid)
    pass

if __name__ == '__main__':
    main()

