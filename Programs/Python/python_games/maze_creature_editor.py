import sys
import os

import json

from lib.default_values import *

import tkinter as tk

import os

class Application(object):

    def __init__(self):
    
        # Create main window
        self.root = tk.Tk()
        self.root.title("Maze Creature Editor")

        self.menubar = tk.Menu(self.root)
        self.menubar.add_command(label = "Quit", command = self.root.destroy)

        self.root.config(menu=self.menubar)
        # List of parameters that users would like to adjust.
        self.list_of_parameters_right = ["creature_name", "hp", "mp", "sp", "ep", "strength", 
        "agility", "vitality", "dexterity", "smartness", "magic_power", "mental_strength", "luckiness"]

        self.list_of_parameters_left = ["exp", "drop_item"]

        self.start_window()
    # The list of parameters that users would like to adjust for creating monsters.

    def start_window(self):
        self.main_group = tk.Frame(self.root)
        self.main_group.pack()

        self.main_list_frame = tk.Frame(self.main_group)
        self.main_list_frame.pack(side = tk.TOP)

        self.main_group_right = tk.Frame(self.main_list_frame)
        self.main_group_right.pack(side = tk.RIGHT, padx = 3, pady =3, anchor = tk.N)

        self.main_group_left = tk.Frame(self.main_list_frame)
        self.main_group_left.pack(side = tk.LEFT, padx = 3, pady =3)

            
        for i,parameter_list in enumerate(self.list_of_parameters_right):
            exec("""self.{0}_adjust_label = tk.Label(self.main_group_left, text = "{0}: " )""". format(parameter_list))
            exec("self.{0}_adjust_label.grid(row = i, sticky = tk.E,column = 0, padx = 3, pady =1)". format(parameter_list))
            exec("self.{0}_input_box = tk.Entry(self.main_group_left)". format(parameter_list))
            exec("self.{0}_input_box.grid(row = i, column = 1, padx = 10, pady =1)". format(parameter_list))
        
        for i,parameter_list in enumerate(self.list_of_parameters_left):
            exec("""self.{0}_adjust_label = tk.Label(self.main_group_right, text = "{0}: " )""". format(parameter_list))
            exec("self.{0}_adjust_label.grid(row = i, sticky = tk.NE,column = 0, padx = 3, pady =1)". format(parameter_list))
            exec("self.{0}_input_box = tk.Entry(self.main_group_right)". format(parameter_list))
            exec("self.{0}_input_box.grid(row = i, column = 1, padx = 10, pady =1, sticky = tk.N)". format(parameter_list))

        self.exit_button = tk.Button(self.main_group, text = "exit", command = exit)
        self.exit_button.pack(side = tk.BOTTOM)

        self.save_button = tk.Button(self.main_group, text = "save", command = self.save_monster_data)
        self.save_button.pack(side = tk.BOTTOM)



        self.root.mainloop()

    def save_monster_data(self):

        file_path = os.path.join(data_dir,creature_data_file_name)

        # 1. Check folder existence
        if not os.path.isdir(data_dir):
            os.mkdir(data_dir)

        # 2. Check file existence
        if not os.path.isfile(file_path):
            open(file_path, 'a').close()
        
        # Main frame for putting monster
        main_creature_data = {}

        # Get creature name
        main_creature_name = eval("self.creature_name_input_box.get()")
        tmp = {}

        with open(file_path, "r") as f:
            string = f.read()
            if string != "":
                main_creature_data = json.loads(string)
            else:
                main_creature_data = {}

        # try:
            # Check whether the game data exist...

        for i in self.list_of_parameters_right[1:]:
            exec("tmp[i] = int(self.{0}_input_box.get())".format(i))

        exec("""tmp["{0}"] = self.{0}_input_box.get()""".format("drop_item"))
        exec("""tmp["{0}"] = int(self.{0}_input_box.get())""".format("exp"))

        # Put & update the data of main creature data.
        main_creature_data[main_creature_name] = tmp

        with open(file_path, "w") as f:
            f.write(json.dumps(main_creature_data, indent = 4))
            
        # except :
        #     print("Please input a proper value.")

# Start the application
def main():
    Application()

if __name__ == '__main__':
    main()


