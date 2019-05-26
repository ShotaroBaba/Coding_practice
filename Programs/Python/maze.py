# import os, pygame
# from pygame.locals import *
# from pygame.compat import geterror
# import time

from random import shuffle
from random import randint
randint(1,2)
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

def make_maze_grid(width = height_default, height = width_default):

    grid = [[[] for _ in range(width)] for _ in range(height)]

    # Take grid as the numbers
    def generate_maze_grid(current_x=0,current_y=0):
        
        move_directions = ["N","S","E","W"]

        shuffle(move_directions)

        for move_direction in move_directions:
            
            next_x = current_x + direction[move_direction][0]
            next_y = current_y + direction[move_direction][1]

            if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid) and grid[next_x][next_y] == []:
                grid[current_x][current_y].append(opposite_direction[move_direction])
                grid[next_x][next_y].append(move_direction)
                generate_maze_grid(next_x, next_y)

    generate_maze_grid(randint(0, width-1), randint(0, height-1))

    return grid

# Create maze first.
def print_maze_grid(grid):
    # Print maze based on the information on grid.
    # String used for generating maze.
    maze_str = ""

    range_x = range(2 * len(grid[0]) + 1)
    range_y = range(2 * len(grid) + 1)
    max_x = len(list(range_x)) - 1
    max_y = len(list(range_y)) - 1
    for y in range_y:
        for x in range_x:
            if x % 2 == 1 and y % 2 == 1: 
                maze_str += " "
            elif x % 2 == 0 and y % 2 == 1:
                if (x == 0 or x == max_x):
                    maze_str += "w"
                else:
                    # if W --> E
                    if "W" in grid[x//2-1][y//2] and "E" in grid[x//2][y//2]:
                        maze_str += " "
                    # if not, the wall is retained.
                    else:
                        maze_str += "w" 
            elif y % 2 == 0 and x % 2 == 1:
                if(y == 0 or y == max_y):
                    maze_str += "w"
                else:
                    # if N --> S, then the wall is removed.
                    if "N" in grid[x//2][y//2 -1] and "S" in grid[x//2][y//2]:
                
                        maze_str += " "
                    # if not, the wall is retained.
                    else:
                        maze_str += "w" 
            else:
                maze_str += "w"
        maze_str += "\n"
    print(maze_str)

    return maze_str

# Create maze first.
def print_maze_grid_test(grid):
    # Print maze based on the information on grid.

    # String used for generating maze.
    maze_str = ""

    for y in range(2 * len(grid[0]) + 1):
        for x in range(2 * len(grid) + 1):
            if x % 2 == 1 and y % 2 == 1:
                maze_str += " "
            else:
                maze_str += "w"
        maze_str += "\n"
    print(maze_str)


grid = make_maze_grid(10,10)
print_maze_grid_test(grid)
print_maze_grid(grid)

# TODO: Putting codes in the main program.
def main():
    grid = make_maze_grid()

    print(grid)
    pass

if __name__ == '__main__':
    main()

