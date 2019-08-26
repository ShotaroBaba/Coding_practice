
import sys
sys.path.insert(0, 'lib/maze_generation.py')
sys.path.insert(0, 'lib/getch.py')

# Set the colors of characters in the terminal.
import os
os.system("color 0") 
from copy import deepcopy

from random import shuffle
from random import randint
from random import choice

from lib.getch import _Getch
from lib.clear_screen import clear

from lib.maze_generation import generate_maze_grid, make_maze_grid


getch = _Getch()

# Initialize and set directions
direction = {"N": (0,-1), "S":(0,1),"E":(1,0), "W":(-1,0)}

# Set the directions to create...
arrow_key_to_directions = {"UP_KEY": "N", "DOWN_KEY": "S", "RIGHT_KEY": "E", "LEFT_KEY": "W"}

# TODO: Difficulty will be selected

# TODO: Separate the components and put them into different files

# TODO: Create methods for saving and loading game

# TODO: Sometimes, the change of the value can only be applied during the fights.

# Save all objects into json format.
def load_data():
    pass

# Load all objects into json format.
def save_data():
    pass

# Used for a player, an enemy and a non-player character class
# TODO: Find the class name that is suitable for explanation
class MazeObject(object):

    # Read the json object to initalise the data, 
    def __init__(self, json_data = {}):
        
        # The enemy and player level, which is an important value.
        self.level = 1 

        # hp: Hit point
        # mp: Magic point
        # sp: Stamina point
        # ep: Energy point
        self.hp = json_data["hp"] if json_data != {} else 100
        self.mp = json_data["mp"] if json_data != {} else 100
        self.sp = json_data["sp"] if json_data != {} else 100
        self.ep = json_data["ep"] if json_data != {} else 100

        # Object's parameters
        self.strength = json_data["strength"] if json_data != {} else 10
        self.agility = json_data["agility"] if json_data != {} else 10
        self.vitality = json_data["vitality"] if json_data != {} else 10
        self.dexterity = json_data["dexterity"] if json_data != {} else 10

        self.smartness = json_data["smartness"] if json_data != {} else 10
        self.magic_power = json_data["magic_power"] if json_data != {} else 10
        self.mental_strength = json_data["mental_strength"] if json_data != {} else 10

        # TODO: Implement luckiness effects
        self.luckiness = json_data["luckiness"] if json_data != {} else 10

        # Check whether it is a player, an enemy or just an object
        self.player_name = json_data["player_name"] if json_data != {} else "None"
        self.is_living = json_data["is_living"] if json_data != {} else True
        self.is_player = json_data["is_player"] if json_data != {} else True
        self.is_enemy = json_data["is_enemy"] if json_data != {} else  False

        # Show the objects that player wields.
        self.right_arm = json_data["right_arm"] if json_data != {} else "Empty"
        self.left_arm = json_data["left_arm"] if json_data != {} else "Empty"

        self.head = json_data["head"] if json_data != {} else "Empty"
        self.arm =  json_data["arm"] if json_data != {} else "Empty"
        self.leg = json_data["leg"] if json_data != {} else "Empty"
        self.wrist = json_data["wrist"] if json_data != {} else "Empty"

        self.right_finger = json_data["right_finger"] if json_data != {} else "Empty"
        self.left_finger = json_data["left_finger"] if json_data != {} else "Empty"

        # Initialise paramteres based on player's equipment.
        self._init_parameters_equipment()

        # Status is normal by default
        # if the status is normal, then the player is not affected.
        self.status = json_data["status"] if json_data != {} else "Normal"

        # By default, the Objects's position is unknown.
        # It is only applied to the player.
        self.object_pos = json_data["object_pos"] if json_data != {} else None

        # Check how the character is displayed.
        self.displayed_character = json_data["displayed_character"] if json_data != {} else "@"

        # The maximum number of items that Objects can hold
        # It can be increased by the level up.
        self.max_item_hold = json_data["max_item_hold"] if json_data != {} else 10

        # Objects's current hit point
        self.exp = json_data["exp"] if json_data != {} else 0

        # Objects's necessary experience points.
        self.next_exp = json_data["next_exp"] if json_data != {} else 100

        # Item numbers is recorded in the dictionary type
        self.items = json_data["items"] if json_data != {} else {}

        # TODO Create the skill classes for users
        self.skills = json_data["skills"] if json_data != {} else {}

        # Rank that can be used for adjusting the random encounter in dungeon.
        self.rank = json_data["rank"] if json_data != {} else {}

    # Apply skills to a certain person, enemy or items
    def use_skills(self, skill_name, target):
        self.skills[skill_name].activate_skills(target)
        pass

    # Adjust parameters based on the equipment
    def _init_parameters_equipment(self):
        pass

    # Experience gained after the battles or through the items.
    def gained_exp(self):
        pass

    # Player can wear his or her own weapon, accessory or armor
    def attach_item(self, item):
        pass

    # Player can remove his or her own weapon, accessory or armor
    def detach_item(self, item):
        pass

    def _initialise_json(self):
        pass

    # Initialise player when the game is started.
    def initialise_player(self):
        pass


    # Used for generating json data for saving character's data.
    def return_character_data_json(self):
        pass

    # Move characters when the enemy
    def move_object_up(self, key_event):
        pass

    def move_object_down(self, key_event):
        pass

    def move_object_left(self, key_event):
        pass
    
    def move_object_right(self, key_event):
        pass



# This includes passive skills and active skills used by player, enemy and objects.
# This can be anything, fighting enemy, saving data and so forth.
# Load all of the skills.

# TODO: The first task is to implement "Attack" skills
class Skills(object):

    # The way to initialise the object is to use the JSON object files.    
    def __init__(self, json_file = {}):

        # The spend mp and hp for using skills
        # They are often fixed or random value
        self.hp_change = hp_change
        self.mp_change = mp_change
        self.sp_change = sp_change
        self.ep_change = ep_change
        self.is_random = None
        # Random is FALSE by default
        self.is_random_point_change = False
        self.is_random_skill_points = False

        # Set the skill levels to adjust their effectiveness
        self.skill_level = 0

        # Ignore the effects caused by the values when the skills
        # are activated. It is False by default.
        self.is_skill_points_ignored = False
        self.item_weight = False

        self.random_range = 1.05

    # Target can be the persons, or enemies
    def activate_skills(self, target):
        if self.is_random:
            pass
        else:
            pass

# This is an item class, this includes weapon, shields and potions.
# Item might also have the skills in some cases.

class Items(object):
    def __init__(self, json_data = {}):
        # The values of changes of the status values
        self.status_change = ""

        # When used, the item will creates the following effects if they have...
        self.hp_change = json_data["hp_change"] if json_data != {} else 100
        self.mp_change = json_data["mp_change"] if json_data != {} else 100
        self.sp_change = json_data["sp_change"] if json_data != {} else 100
        self.ep_change = json_data["ep_change"] if json_data != {} else 100

        self.strength_change = json_data["strength_change"] if json_data != {} else 10
        self.agility_change  = json_data["agility_change"] if json_data != {} else 10
        self.vitality_change  = json_data["vitality_change"] if json_data != {} else 10
        self.dexterity_change  = json_data["dexterity_change"] if json_data != {} else 10

        self.smartness_change  = json_data["smartness_change"] if json_data != {} else 10
        self.magic_power_change  = json_data["magic_power_change"] if json_data != {} else 10
        self.mental_strength_change  = json_data["mental_strength_change"] if json_data != {} else 10
        
        # TODO: Implement luckiness effects
        self.luckiness = json_data["luckiness"] if json_data != {} else 10
        
        self.durablity_change = json_data["durablity_change"] if json_data != {} else 10



# TODO: Create the enchantment class.
class Enchantment(object):
    def __init__(self):
        pass

 
# The map for players to walk at the beginning
class Map(object):

    # When initialised, Map object puts players and item boxes at the
    # places.
    def __init__(self, width, height):
        clear()
        self.map_grid = generate_maze_grid(make_maze_grid(width,height))
        self.original_map_grid = deepcopy(self.map_grid)

        self.hidden_map_grid = [["." for _ in range(len(self.map_grid))] for _ in range(len(self.map_grid[0]))]

        self.direction = direction

        # Test purpose for putting player.
        self.player = MazeObject()

        self.randomly_place_player(self.player)

        self.draw_map()
    
    # It is called every time the cursor is moved.
    def move_player(self,str_direction):
        pos_move = direction[arrow_key_to_directions[str_direction]]
        next_player_pos = (self.player.object_pos[0] + pos_move[0],self.player.object_pos[1] + pos_move[1])
        if self.original_map_grid[next_player_pos[0]][next_player_pos[1]] != "#":
            clear()

            # Initialize map using originally created random map.
            self.map_grid = deepcopy(self.original_map_grid)

            # Place player on the map based on the move player made.
            self.map_grid[next_player_pos[0]][next_player_pos[1]] = self.player.displayed_character

            # Update player position.
            self.player.object_pos = next_player_pos

            # Draw new map.
            self.draw_map()

    # Randomly place player
    def randomly_place_player(self,player):
        space_list_to_place_player = []
        for y in range(len(self.map_grid[0])):
            for x in range(len(self.map_grid)):
                if self.map_grid[x][y] == " ":
                    space_list_to_place_player.append((x,y))
        
        # Choose the place where the player can begin journey
        chosen_place = choice(space_list_to_place_player)
        self.map_grid[chosen_place[0]][chosen_place[1]] = self.player.displayed_character
        self.player.object_pos = chosen_place

    # TODO: All the information of the map is hidden at the beginning.
    def _reveal_maps_by_walking(self):
        pass

    # Draw the map on the screen.
    def draw_map(self):
        tmp_str = ""
        # NOTE: x: height, y: length
        for y in range(len(self.map_grid[0])):
            for x in range(len(self.map_grid)):
                if self.map_grid[x][y] == "@":
                    tmp_str += "\033[91m" + self.map_grid[x][y] + "\033[0m"
                else:
                    tmp_str += self.map_grid[x][y]
            tmp_str += "\n"
        # print(self.map_grid)
        
        # Print map
        print(tmp_str)

    # Saves the data of the maps into json file.
    def save_map_data(self):
        pass

# Display menu so that users are able to control a person.
# TODO: Create the menu class

# Create the object to start the game...
class MainGame():
    def __init__(self):
        self.first_map = Map(10, 10)
        self.manipulate_map()

    def manipulate_map(self):
        while True:
            character = getch()
            if character == b"n":
                break
            else:
                if character in ["UP_KEY", "DOWN_KEY", "LEFT_KEY", "RIGHT_KEY"]:
                    self.first_map.move_player(character)
        
        # TODO: Random encounter needed to be implemented.

class Menu(object):
    def __init__(self):
        pass

    # Draw menu.
    def draw_menu(self):
        pass

# TODO: Putting codes that allows player to move in the main program.
# Create first main game here.
def main():
    main_game = MainGame()

if __name__ == '__main__':
    main()

