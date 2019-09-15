
# Item has a number of effects.

# TODO: Implement temporary status changes.

# TODO: Power up the items as the level goes up...

class Items(object):
    def __init__(self, json_data = {}, level = 1):
        
        # The values of changes of the status values
        self.status_change = ""

        # Item name
        self.item_name = json_data["item_name"] if json_data != {} else 0

        # When used, the item will creates the following effects if they have...
        self.hp_change = json_data["hp_change"] if json_data != {} else 0
        self.mp_change = json_data["mp_change"] if json_data != {} else 0
        self.sp_change = json_data["sp_change"] if json_data != {} else 0
        self.ep_change = json_data["ep_change"] if json_data != {} else 0

        self.strength_change = json_data["strength_change"] if json_data != {} else 0
        self.agility_change  = json_data["agility_change"] if json_data != {} else 0
        self.vitality_change  = json_data["vitality_change"] if json_data != {} else 0
        self.dexterity_change  = json_data["dexterity_change"] if json_data != {} else 0

        self.smartness_change  = json_data["smartness_change"] if json_data != {} else 0
        self.magic_power_change  = json_data["magic_power_change"] if json_data != {} else 0
        self.mental_strength_change  = json_data["mental_strength_change"] if json_data != {} else 0
        self.is_cure_status = json_data["is_cure_status"] if json_data != {} else False

        # Luckiness effect changes the possibility of dropping items from enemy.
        self.luckiness = json_data["luckiness_change"] if json_data != {} else 0
        self.effective_time = json_data["effective_time"] if json_data != {} else 0

        self.durablity_change = json_data["durablity_change"] if json_data != {} else 0

        self.weight = json_data["weight"] if json_data != {} and "" else 10

    def update_item(self):
        self.effective_time -= 1

