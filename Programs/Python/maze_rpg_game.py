
from random import shuffle
from random import randint

# This game will become Role Playing Game where a person 
# walks around the maze and fights with foes. Backtracing algorithm is used
# for generating maze.

# Initiall create the grid
# The form of the grid is as follows:

direction = {"N": (0,-1), "S":(0,1),"E":(1,0), "W":(-1,0)}
opposite_direction  = {"N":"S", "S":"N", "E":"W", "W":"E"}
# Firstly, make grid using list.
# height and width must be number

height_default = 5
width_default = 5

# Python Player class.
class Player(object):

    # hp: Hit point
    # mp: magic point
    # ep: energy point
    self.hp = 100
    self.mp = 100
    self.ep = 100

    # The maximum number of items that player can hold
    self.max_item_hold = 10

    # Player's current hit point
    self.exp = 0

    # Player's necessary experience points.
    self.next_exp = 100

    # Item numbers is recorded in the dictionary type.
    self.items = {}

    # TODO Create the skill classes for users
    self.skills = None

# This includes passive skills and active skills
# Skills can be anything.
class Skills(object):
    
    def __init(self):

        # The spend mp and hp for using skills
        self.spend_mp = 0
        self.spend_hp = 0


        
    pass

# This is an item class, this includes weapon, shields and potions.
# Item might have the skills in some cases.
class Items(object):
    pass

# Python Enemy class.
# Currently, there is no images for foes.
class Foe(object):

    pass

def make_maze_grid(width = height_default, height = width_default):

    grid = [[[] for _ in range(width)] for _ in range(height)]

    # Take grid as the numbers
    def generate_maze_grid(current_x=0,current_y=0):
        
        move_directions = ["N","S","E","W"]

        shuffle(move_directions)

        for move_direction in move_directions:
            
            next_x = current_x + direction[move_direction][0]
            next_y = current_y + direction[move_direction][1]

            if 0 <= next_x < len(grid[0]) and 0 <= next_y < len(grid) and grid[next_y][next_x] == []:
                grid[current_y][current_x].append(opposite_direction[move_direction])
                grid[next_y][next_x].append(move_direction)
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
                    if "W" in grid[y//2][x//2-1] and "E" in grid[y//2][x//2]:
                        maze_str += " "
                    # if not, the wall is retained.
                    else:
                        maze_str += "w" 
            elif y % 2 == 0 and x % 2 == 1:
                if(y == 0 or y == max_y):
                    maze_str += "w"
                else:
                    # if N --> S, then the wall is removed.
                    if "N" in grid[y//2 -1][x//2]and "S" in grid[y//2][x//2]:
                
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


grid = make_maze_grid(50,10)
print_maze_grid_test(grid)
print_maze_grid(grid)

# TODO: Putting codes in the main program.
def main():
    grid = make_maze_grid()

    print(grid)
    pass

if __name__ == '__main__':
    main()

