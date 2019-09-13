
# Reading all necessary packages
import sys
sys.path.insert(0, 'lib/maze_generation.py')
sys.path.insert(0, 'lib/getch.py')

import os
import json 
from copy import deepcopy
from random import shuffle
from random import randint
from random import choice
from random import uniform
from lib.getch import _Getch
from lib.clear_screen import clear
from lib.maze_generation import generate_maze_grid, make_maze_grid
from random import random
from lib.maze_object import MazeObject

from lib.default_values import *

constant_next_level_exp = 1.4

# Load creatures.
creature_file_path = os.path.join(data_dir,monster_data_file_name)
enemy_json = json.loads(open(creature_file_path, "r").read())


# Set the colors of characters in the terminal.
os.system("color 0") 

# TODO: Create at least one creature.
enemy_json_list = []

getch = _Getch()

# Initialize and set directions
direction = {"N": (0,-1), "S":(0,1),"E":(1,0), "W":(-1,0)}

# Set the directions to create...
arrow_key_to_directions = {"UP_KEY": "N", "DOWN_KEY": "S", "RIGHT_KEY": "E", "LEFT_KEY": "W"}

default_ememy_encounter = 0.2
min_enemy_encounter = 0.1

numerical_player_strengh = ["hp", "mp", "sp", "ep"]
non_numerical_player_strength = ["strength", "agility", "vitality", "dexterity", "smartness", "magic_power", "mental_strength"]   

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
# TODO: Change Map name to a proper name
class Map(object):

    # When initialised, Map object puts players and item boxes at the
    # places.
    def __init__(self, width, height):
        # Clear the screen before drawing map
        self.width = width
        self.height = height
        self.level = 1

        # Set the symbols below this line:
        self.goal_symbol = "\033[93m" + "G" + "\033[0m"
        self.treasure_symbol = "\033[36m" + "T" + "\033[0m"
        self.treasure_taken_symbol = None
        self._initialize_map()
        clear()

        self.draw_map()
    
        self._manipulate_map_main_menu()

    
    def _manipulate_map_main_menu(self):
        while True:
            character = getch()
            
            # This condition will be removed later.
            if character == b"n":
                break
            else:
                if character in ["UP_KEY", "DOWN_KEY", "LEFT_KEY", "RIGHT_KEY"]:
                    self.move_player(character)
                elif character == b"\x1b":
                    self.player_menu()


    # Turn-based fight is now imminent
    # TODO: Enable the random appearance of the enemy based on the depth of the level.
    # TODO: Enable to fight several enemies.

    def _enemy_fight(self):
        
        # TODO: Adding the fights between enemy and player
        # Create selection screen
        selection_list = ["Fight", "Skills", "Item", "Escape"]
        cursor_not_selected = " "
        cursor_selected = ">"
        tmp_cursor = deepcopy(selection_list)
        cursor_selection = 0

        # TODO: Create the alogirhtms that generates the enemy
        
        random_enemy = choice(list(enemy_json.keys()))
        enemy = MazeObject(json_data = enemy_json[random_enemy], level = self.level, is_random="yes")


        def player_turn_normal_attack():
            # Player turn
            player_base_attack_value = self.player.strength
            player_attack_value = int(round(uniform(0.8,1.0) * player_base_attack_value, 0))
            enemy.hp -= player_attack_value
            
            if enemy.hp < 1:
                print("You defeated the creature!")
                print("Player acquire {} exp".format(enemy.exp))
                print("Press any key to return to map...")
                self.player.get_experience(enemy.exp)
                getch()
                clear()
                return True
            else:
                print("Player delivers {} damage".format(player_attack_value))
                getch()
                return False

        def enemy_turn_normal_attack():
            # Enemy turn
            enemy_base_attack_value = enemy.strength
            enemy_attack_value = int(round(uniform(0.8,1.0) * enemy_base_attack_value, 0))
            self.player.hp -= enemy_attack_value
            
            if self.player.hp < 1:
                print("You are defeated...")
                print("Game Over...")
                getch()
                clear()
                return True

            else:
                print("Enemy delivers {} damage".format(enemy_attack_value))
                getch()
                return False


        # Displayed for generating 
        while True:

            for i in range(len(tmp_cursor)):
                if i == cursor_selection:
                    tmp_cursor[i] = cursor_selected + tmp_cursor[i]
                else:
                    tmp_cursor[i] = cursor_not_selected + tmp_cursor[i]

            print("{} appears!".format(random_enemy))
            self.display_status()
            print("\n".join(tmp_cursor))
            tmp_cursor = deepcopy(selection_list)
            tmp = getch()

            if tmp == "UP_KEY":
                if cursor_selection > 0:
                        cursor_selection -= 1
                
            elif tmp == "DOWN_KEY":
                if cursor_selection < len(tmp_cursor) - 1:
                        cursor_selection += 1

            elif tmp == b"\r":

                # Normally attack the enemy.
                if cursor_selection == 0:

                    # Turn based fight. However, the player can firstly fight for the enemy.
                    if uniform(0.8, 1.0)*self.player.agility > uniform(0.8,1.0)* enemy.agility:
                        if player_turn_normal_attack():
                            break
                        if enemy_turn_normal_attack():
                            break

                    else:
                        if enemy_turn_normal_attack():
                            break
                        if player_turn_normal_attack():
                            break
                    
                # TODO: Create the function that handles player's skills.
                if cursor_selection == 1:
                    
                    clear()
                    break

                # Escape from the enemy
                # The rate of the escape depends on the values of
                # the success.
                if cursor_selection == 2:
                    
                    clear()
                    break
                if cursor_selection == 3:

                    clear()
                    break

            clear()

    # TODO: The encounter percentage must be changed
    # Take the luck of the player into account.
    def enemy_encounter(self, player_luck_value):
        k = random()

        # TODO: Make the possibility calculation possible...
        tmp = max(default_ememy_encounter, min_enemy_encounter)

        if 0 < k and k < tmp:
            self._enemy_fight()

    def _initialize_map(self):
        self.map_grid = generate_maze_grid(make_maze_grid(self.width,self.height))

        # Randomly place objects, including goals and treasure boxes.
        self.randomly_place_objects(self.goal_symbol)
        
        for _ in range(randint(0,10)):
            self.randomly_place_objects(self.treasure_symbol)
        
        self.original_map_grid = deepcopy(self.map_grid)

        # TODO: Create and show the hidden map grid.
        self.hidden_map_grid = [["." for _ in range(len(self.map_grid))] for _ in range(len(self.map_grid[0]))]

        self.direction = direction
        
        # Test purpose for putting player.
        self.player = MazeObject()

        # Randomly place goal
        self.randomly_place_player(self.player)

    def _move_player_sub(self,str_direction, next_player_pos):
        # Initialize map using originally created random map.
        self.map_grid = deepcopy(self.original_map_grid)

        # Place player on the map based on the move player made.
        self.map_grid[next_player_pos[0]][next_player_pos[1]] = self.player.displayed_character

        # Update player position.
        self.player.object_pos = next_player_pos

    # Allows the users to select whether they will proceed to the next floor...
    def _map_proceed_selection(self):
        clear()
        
        selection_list = ["Yes", "No"]
        cursor_not_selected = " "
        cursor_selected = ">"
        tmp_cursor = deepcopy(selection_list)
        cursor_selection = 1
        
        while True:
            self.draw_map()
            for i in range(len(tmp_cursor)):
                if i == cursor_selection:
                    tmp_cursor[i] = cursor_selected + tmp_cursor[i]
                else:
                    tmp_cursor[i] = cursor_not_selected + tmp_cursor[i]

            print("Will you proceed to the next level?")
            print("".join(tmp_cursor))

            tmp_cursor = deepcopy(selection_list)
            tmp = getch()
            if tmp == "LEFT_KEY":
                if cursor_selection > 0:
                        cursor_selection -= 1
                
            elif tmp == "RIGHT_KEY":
                if cursor_selection < len(tmp_cursor) - 1:
                        cursor_selection += 1

            elif tmp == b"\r":
                # Yes case --> Initialise map.
                if cursor_selection == 0:
                    
                    self._initialize_map()
                    self.level += 1
                    break
                
                # No case --> Do nothing.
                if cursor_selection == 1:
                    break
            clear()


    def display_status(self):
        print("HP: {}, MP: {}, SP: {}, EP: {}".format(self.player.current_hp, 
        self.player.current_mp,
        self.player.current_sp, 
        self.player.current_ep))
    

    def player_menu(self):
        clear()
        
        selection_list = ["Item", "Save", "Exit"]
        cursor_not_selected = " "
        cursor_selected = ">"
        tmp_cursor = deepcopy(selection_list)
        cursor_selection = 1
        
        while True:
            for i in range(len(tmp_cursor)):
                if i == cursor_selection:
                    tmp_cursor[i] = cursor_selected + tmp_cursor[i]
                else:
                    tmp_cursor[i] = cursor_not_selected + tmp_cursor[i]
            
            print("\n".join(tmp_cursor))

            tmp_cursor = deepcopy(selection_list)
            tmp = getch()
            if tmp == "UP_KEY":
                if cursor_selection > 0:
                    cursor_selection -= 1
                
            elif tmp == "DOWN_KEY":
                if cursor_selection < len(tmp_cursor) - 1:
                    cursor_selection += 1

            elif tmp == b"\r":
                # Yes case --> Initialise map.
                if cursor_selection == 0:
                    break
                
                # Next TODO: To create player data save.
                # No case --> Do nothing.
                if cursor_selection == 1:
                    break
                
                # 
                if cursor_selection == 2:
                    break
            
            elif tmp == b"\x1b":
                clear()
                self.draw_map()
                break

            clear()

        
        pass

    # It is called every time the cursor is moved.
    def move_player(self,str_direction):
        
        pos_move = direction[arrow_key_to_directions[str_direction]]
        next_player_pos = (self.player.object_pos[0] + pos_move[0],self.player.object_pos[1] + pos_move[1])
        
        # If there is a collision, then it will simply draw the map.
        if self.original_map_grid[next_player_pos[0]][next_player_pos[1]] == self.goal_symbol:
           
            clear()

            # Enemy appears before reaches a goal.
            self.enemy_encounter(self.player.luckiness)


            self._move_player_sub(str_direction, next_player_pos)
            # TODO: Allow player to select yes or no to proceed to the next level.
            self._map_proceed_selection()

            clear()
            self.draw_map()

        elif self.original_map_grid[next_player_pos[0]][next_player_pos[1]] != "#":
            clear()

            self._move_player_sub(str_direction, next_player_pos)
            
            # Draw the enemy encouter screen.
            self.enemy_encounter(self.player.luckiness)

            self.draw_map()
            
        else:
            clear()
            self.draw_map()
    
    # Appears when pressing escape button.


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

    def randomly_place_objects(self, symbol_to_use):
        
        # Only one goal can be created
        # Choose the place for a goal
        space_list_to_place_goal = []
        for y in range(len(self.map_grid[0])):
            for x in range(len(self.map_grid)):
                if self.map_grid[x][y] == " ":
                    space_list_to_place_goal.append((x,y))
        
        # Choose the location of goal
        chosen_place = choice(space_list_to_place_goal)
        self.map_grid[chosen_place[0]][chosen_place[1]] = symbol_to_use

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
        
        # Print map
        print(tmp_str)
        self.display_status()
        
    # Saves the data of the maps into json file.
    def save_map_data(self):
        pass

# Display menu so that users are able to control a person.
# TODO: Create the menu class

# Create the object to start the game...
class MainGame():
    
    # TODO: The section "Special" will be created...
    
    def __init__(self):
        
        # Start: Start the game from the beginning
        # Load: Load all game status
        # Exit: Leave game to desktop

        self.menu_selection = ["Start", "Load", "Exit"]
        self.selection_cursor = ">"
        self.selection_not_made = " "
        self.start_main_menu()

        # Create 10x10 maps after creating maps.
        self.random_map = Map(10, 10)

    # Check whether it will load the games or not.
    def start_main_menu(self):
        clear()
        # Set the position of cursor.
        cursor_value = 0
        
        # Deep copy the selection values
        tmp = deepcopy(self.menu_selection)
        # Initialize the start menu.
        for i in range(len(tmp)):
            if i == cursor_value:
                tmp[i] = self.selection_cursor + tmp[i]
            else:
                tmp[i] = self.selection_not_made + tmp[i]

        # Create the menu in accordance with player's input.
        while True:
            print("\n".join(tmp))
            character = getch()

            tmp = deepcopy(self.menu_selection)
            # Temporary breaking point for testing program
            if character == b"\r" and cursor_value == 0:
                break
            
            # TODO: Allows to load the data.
            elif character == b"\r" and cursor_value == 1:
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
    

class Menu(object):
    def __init__(self):
        pass

    # Draw menu.
    def draw_menu(self):
        pass

# TODO: Putting codes that allows player to move in the main program.
# Create first main game here.
def main():
    MainGame()

if __name__ == '__main__':
    main()

