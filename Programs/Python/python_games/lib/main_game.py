# Reading all necessary packages
import sys
sys.path.insert(0, 'lib/maze_generation.py')

import os
import json 
from copy import deepcopy
from random import shuffle
from random import randint
from random import choice
from random import uniform
from getch import _Getch
from clear_screen import clear
from maze_generation import generate_maze_grid, make_maze_grid
from random import random
from maze_object import MazeObject

from default_values import *

# The value which determine the difficulty of level increase.
constant_next_level_exp = 1.4

default_amount_to_reveal = 3
# Load creatures.
creature_file_path = os.path.join(data_dir,creature_data_file_name)
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

# Enemy encounter probability is calculated based on the luckiness.
default_ememy_encounter = 0.2
min_enemy_encounter = 0.1

numerical_player_strengh = ["hp", "mp", "sp", "ep"]
current_status_player = ["current_hp", "current_mp", "current_sp", "current_ep"]

non_numerical_player_strength = ["strength", "agility", "vitality",
                                 "dexterity", "smartness", "magic_power", "mental_strength"]   

string_numerical_player_strength = ["player_name", "is_living", "is_player", 
                                    "is_enemy", "arm", "leg", "right_wrist", "left_wrist", 
                                    "right_finger", "left_finger", "status", "displayed_character",
                                    "max_item_hold", "exp", "current_exp", "bonus_point", "next_exp", "items",
                                    "skills", "rank", "drop_item"]

# TODO: Difficulty will be selected

# TODO: Separate the components and put them into different files

# TODO: Create methods for saving and loading game

# TODO: Sometimes, the change of the value can only be applied during the fights.

# Save all objects into json format.
def load_data():
    pass

# The map for players to walk at the beginning
# TODO: Change Map name to a proper name
class MainGame(object):

    # When initialised, Map object puts players and item boxes at the
    # places.

    # When loading the game the game will
    # loaded_map: map to be loaded.
    # loaded_player: player data to be loaded.
    def __init__(self, loaded_map = {}, loaded_player = {}):
        
        # Putting player object first
        # Test purpose for putting player.
        if loaded_player != {}:
            self.load_player_data()
        else:
            self.player = MazeObject()

        # Amount to reveal.
        self.default_amount_to_reveal = default_amount_to_reveal

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

        
        
        # Reveal map grid from the center of the player.
        self.reveal_map_grid()

        self.draw_hidden_map()
        
        self._manipulate_map()

    # Load player's data.
    def load_player_data(self):
        pass
    
    def _manipulate_map(self):
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

    # TODO: Create class for fight screen.
    # It will become too long and complicated if it hasn't done.
    # enemy_fight will handle the map object..
    def _enemy_fight(self):
        
        # TODO: Adding the fights between enemy and player
        # Create selection screen
        selection_list = ["Fight", "Skills", "Item","Status", "Escape"]
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
            enemy.current_hp -= player_attack_value
            
            if enemy.current_hp < 1:
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
            self.player.current_hp -= enemy_attack_value
            
            if self.player.current_hp < 1:
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

                    # Turn based fight. The player can firstly fight for the enemy this value is higher.
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
                elif cursor_selection == 1:    
                    clear()
                    break

                # Escape from the enemy.
                # The rate of the escape depends on the values of
                # the success.
                elif cursor_selection == 2:            
                    clear()
                    break

                elif cursor_selection == 3:
                    clear()
                    break

            clear()

    # TODO: The encounter percentage must be changed
    # Take the luck of the player into account.
    def enemy_encounter(self, player_luck_value):
        k = random()

        # TODO: Make the possibility calculation possible...
        tmp = max(default_ememy_encounter, min_enemy_encounter)

        # Create the object instead of calling function...
        if 0 < k and k < tmp:
            self._enemy_fight()

    def _initialize_map(self):
        self.map_grid = generate_maze_grid(make_maze_grid(self.width,self.height))

        # Randomly place objects, including goals and treasure boxes.
        self.randomly_place_objects(self.goal_symbol)
        
        # Randomly place treasure.
        for _ in range(randint(0,10)):
            self.randomly_place_objects(self.treasure_symbol)
        
        self.original_map_grid = deepcopy(self.map_grid)

        # TODO: Create and show the hidden map grid.
        self.hidden_map_grid = [["." for _ in range(len(self.map_grid))] for _ in range(len(self.map_grid[0]))]
       
        self.direction = direction
        
        # Randomly place goal
        self.randomly_place_player(self.player)

        
    # Reveal the grid of the map based on the player's location.
    def reveal_map_grid(self):

        for i in range(max(0, self.player.object_pos[0] - self.default_amount_to_reveal),\
            min(self.player.object_pos[0] + self.default_amount_to_reveal, len(self.map_grid[0]))):
            for j in range(max(0, self.player.object_pos[1] - self.default_amount_to_reveal),\
                min(self.player.object_pos[1] + self.default_amount_to_reveal, len(self.map_grid))):
                # Find Reveal the maps.
                    self.hidden_map_grid[i][j] = self.map_grid[i][j]

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

            
            self.draw_hidden_map()
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
        
        # There is no load function until player moves to exit.
        selection_list = ["Item", "Save","Status", "Exit"]
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
                    pass

                # Next TODO: To create player data save.
                if cursor_selection == 1:
                    pass
                
                # Displaying player's status, allowing users to
                # improve status using bonus points.
                if cursor_selection == 2:
                    pass
                
                if cursor_selection == 3:
                    pass

                clear()
                self.draw_hidden_map()
                break

            elif tmp == b"\x1b":
                clear()
                self.draw_hidden_map()
                break

            clear()
    
    # Save player's data and attributes.
    def save_data(self):
        # The value for storing player data.
        saved_data_dic = {}
        
        joined_path = os.path.join(save_data_folder, save_data_file_name)

        # If directory does not exist, then it will be created.
        if not os.path.isdir(save_data_folder):
            os.mkdir(save_data_folder)

        # File is created if it does not exist.
        if not os.path.isfile(joined_path):
            open(joined_path, 'a').close()

        for attribute in numerical_player_strengh + current_status_player + non_numerical_player_strength + \
            string_numerical_player_strength:
            exec("""saved_data_dic["{0}"] = self.player.{0}""".format(attribute))

        # Player location is saved

        saved_data_dic["object_pos"] = self.player.object_pos
        
        saved_data_dic["map_grid"] = self.original_map_grid

        with open(joined_path, 'w') as f:
            f.write(json.dumps(saved_data_dic, indent = 4)) 



    def load_data(self):
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
            self.draw_hidden_map()

        elif self.original_map_grid[next_player_pos[0]][next_player_pos[1]] != "#":
            clear()

            self._move_player_sub(str_direction, next_player_pos)
            
            # Draw the enemy encouter screen.
            self.enemy_encounter(self.player.luckiness)

            self.draw_hidden_map()
            
        else:
            clear()
            self.draw_hidden_map()

    

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
    # Will be obsolete.
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

    # Mainly used for drawing maps.
    # Draw the hidden map on the screen.
    def draw_hidden_map(self):
        self.reveal_map_grid()
        tmp_str = ""
        # NOTE: x: height, y: length
        for y in range(len(self.hidden_map_grid[0])):
            for x in range(len(self.hidden_map_grid)):
                if self.hidden_map_grid[x][y] == "@":
                    tmp_str += "\033[91m" + self.hidden_map_grid[x][y] + "\033[0m"
                else:
                    tmp_str += self.hidden_map_grid[x][y]
            tmp_str += "\n"
        
        # Print map
        print(tmp_str)
        self.display_status()


    # Saves the data of the maps into json file.
    def save_map_data(self):
        pass
