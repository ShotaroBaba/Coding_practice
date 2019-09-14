
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

