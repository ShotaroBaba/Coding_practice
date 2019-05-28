
import sys
sys.path.insert(0, 'lib/maze_generation.py')

from random import shuffle
from random import randint
from lib.maze_generation import generate_maze_grid, make_maze_grid


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
        self.displayed_character = json_data["displayed_character"] if json_data != {} else "#"

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

    # Target can be the persons
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
    def __init__():
        pass

 
# The map for players to walk at the beginning
class Map(object):

    # When initialised, Map object puts players and item boxes at the
    # places.

    def __init__(self, width, height):
        self.map = generate_maze_grid(make_maze_grid(width,height))
        pass

    # Saves the data of the maps into json file.
    def save_map_data():
        pass

# Display menu so that users are able to control a person.
# TODO: Create the menu class
class Menu(object):
    def __init__():
        pass



# TODO: Putting codes in the main program.
def main():
    first_map = Map(20,20)
    pass

if __name__ == '__main__':
    main()

