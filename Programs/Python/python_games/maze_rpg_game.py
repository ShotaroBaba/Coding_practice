
import sys
sys.path.insert(0, 'lib/maze_generation.py')
sys.path.insert(0, 'lib/getch.py')

from random import random
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

default_ememy_encounter = 0.2
min_enemy_encounter = 0.1


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

# A number of skills are stored in the json file...
class Skills(object):

    # The way to initialise the object is to use the JSON object files.    
    def __init__(self, json_data = {}):

        # The spend mp and hp for using skills
        # They are often fixed or random value
        self.hp_change = json_data["hp_change"] if json_data != {} else 100
        self.mp_change = json_data["mp_change"] if json_data != {} else 100
        self.sp_change = json_data["sp_change"] if json_data != {} else 100
        self.ep_change = json_data["ep_change"] if json_data != {} else 100
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

        # TODO: Create a part of skills describing upgrade
    # Target can be the persons, or enemies
    def activate_skills(self, target):
        if self.is_random:
            pass
        else:
            pass

# This is an item class, this includes weapon, shields and potions.
# Item might also have the skills in some cases.

# Item has a number of effects.
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
        # Luckiness effect changes the possibility of dropping items from enemy.
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
        # Clear the screen before drawing map
        self.width = width
        self.height = height

        # Set the symbols below this line:
        self.goal_symbol = "\033[93m" + "G" + "\033[0m"
        self._initialize_map()
        clear()

        # Set the map_grid.

        self.draw_map()
    
    # Turn-based fight is now imminent
    def enemy_fight(self, player, level = 1):
            
        # TODO: Adding the fights between enemy and player
            
        # Clear the screen before the fight begins
        clear()

            # Just a test screen for the development
        character = getch()

        # Temporary breaking point for testing program
        while True:

            character = getch()
            print("This is only the test fight.")
            print("The material will be added later on...")
            
            if character == b"n":
                clear()
                break

    # TODO: The encounter percentage must be changed
    # Take the luck of the player into account.
    def enemy_encounter(self, player_luck_value):
        k = random()

        # TODO: Make the possibility calculation possible...
        tmp = max(default_ememy_encounter, min_enemy_encounter)

        if 0 < k and k < tmp:
            self.enemy_fight(self, self.player)

    def _initialize_map(self):
        self.goal_pos = None
        self.map_grid = generate_maze_grid(make_maze_grid(self.width,self.height))
        self.randomly_place_objects()
        self.original_map_grid = deepcopy(self.map_grid)
        self.hidden_map_grid = [["." for _ in range(len(self.map_grid))] for _ in range(len(self.map_grid[0]))]

        self.direction = direction

        # Test purpose for putting player.
        self.player = MazeObject()

        # Randomly place goal
        self.randomly_place_object(self.player)

    def _move_player_sub(self,str_direction, next_player_pos):
        # Initialize map using originally created random map.
        self.map_grid = deepcopy(self.original_map_grid)

        # Place player on the map based on the move player made.
        self.map_grid[next_player_pos[0]][next_player_pos[1]] = self.player.displayed_character

        # Update player position.
        self.player.object_pos = next_player_pos

    # It is called every time the cursor is moved.
    def move_player(self,str_direction):
        
        pos_move = direction[arrow_key_to_directions[str_direction]]
        next_player_pos = (self.player.object_pos[0] + pos_move[0],self.player.object_pos[1] + pos_move[1])
        
        # If there is a collision, then it will simply draw the map.
        if self.original_map_grid[next_player_pos[0]][next_player_pos[1]] == self.goal_symbol:
           
            clear()

            # Enemy appears before reaches a goal.
            self.enemy_encounter(self.player.luckiness)

            # TODO: Allow player to select yes or no to proceed to the next level.
            self._initialize_map()

            self.draw_map()

        elif self.original_map_grid[next_player_pos[0]][next_player_pos[1]] != "#":
            clear()

            self._move_player_sub(str_direction, next_player_pos)
            
            # Draw new map.
            self.enemy_encounter(self.player.luckiness)
            self.draw_map()

        else:
            clear()
            self.draw_map()
            


    # Randomly place player
    def randomly_place_object(self,player):
        space_list_to_place_player = []
        for y in range(len(self.map_grid[0])):
            for x in range(len(self.map_grid)):
                if self.map_grid[x][y] == " ":
                    space_list_to_place_player.append((x,y))
        
        # Choose the place where the player can begin journey
        chosen_place = choice(space_list_to_place_player)
        self.map_grid[chosen_place[0]][chosen_place[1]] = self.player.displayed_character
        self.player.object_pos = chosen_place

    def randomly_place_objects(self):
        
        # Only one goal can be created
        # Choose the place for a goal
        space_list_to_place_goal = []
        for y in range(len(self.map_grid[0])):
            for x in range(len(self.map_grid)):
                if self.map_grid[x][y] == " ":
                    space_list_to_place_goal.append((x,y))
        
        # Choose the location of goal
        chosen_place = choice(space_list_to_place_goal)
        self.map_grid[chosen_place[0]][chosen_place[1]] = self.goal_symbol
        self.goal_pos = chosen_place

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
    
    # TODO: The section "Special" will be created...
    
    def __init__(self):
        self.menu_selection = ["Start", "Load", "Exit"]
        self.selection_cursor = ">"
        self.selection_not_made = " "
        self.start_main_menu()
        self.random_map = Map(10, 10)
        self.manipulate_map()

    # Check whether it will load the games or not.
    def start_main_menu(self):

        # Set the position of cursor.
        cursor_value = 0
        
        tmp = deepcopy(self.menu_selection)

        # Initialize the start menu.
        for i in range(len(tmp)):
            if i == cursor_value:
                tmp[i] = self.selection_cursor + tmp[i]
            else:
                tmp[i] = self.selection_not_made + tmp[i]
        clear()
        print("\n".join(tmp))

        # Create the menu in accordance with player's input.
        while True:
            character = getch()
            tmp = deepcopy(self.menu_selection)

            # Temporary breaking point for testing program
            if character == b"n":
                break
            else:
                if character == "UP_KEY":
                    if cursor_value > 0:
                        cursor_value -= 1
                elif character == "DOWN_KEY":
                    if cursor_value < len(self.menu_selection) - 1:
                        cursor_value += 1

            for i in range(len(tmp)):
                
                if i == cursor_value:
                    tmp[i] = self.selection_cursor + tmp[i]
                
                else:
                    tmp[i] = self.selection_not_made + tmp[i]
            clear()
            print("\n".join(tmp))

    def manipulate_map(self):
        while True:
            character = getch()
            if character == b"n":
                break
            else:
                if character in ["UP_KEY", "DOWN_KEY", "LEFT_KEY", "RIGHT_KEY"]:
                    self.random_map.move_player(character)

    

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

