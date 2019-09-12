import tkinter as tk


class Application(object):

    def __init__(self):
    
        # Create main window
        self.root = tk.Tk()
        self.root.title("Monster editor")

        self.menubar = tk.Menu(self.root)
        self.menubar.add_command(label = "Quit", command = self.root.destroy)

        self.root.config(menu=self.menubar)
        # List of parameters that users would like to adjust.
        self.list_of_parameters_right = ["monster_name","start to appear", "hp", "mp", "sp", "ep"]

        self.start_window()
    # The list of parameters that users would like to adjust for creating monsters.

    def start_window(self):
        self.main_group = tk.Frame(self.root)
        self.main_group.pack()

        self.main_group_right = tk.Frame(self.main_group)
        self.main_group_right.pack(side = tk.RIGHT)

        self.main_group_left = tk.Frame(self.main_group)
        self.main_group_left.pack(side = tk.LEFT)
        
        self.main_group_right_hp = tk.Frame(self.main_group_right)
        self.main_group_right_hp.pack()
        """
        self.hp_adjust_label = tk.Label(self.main_group_right_hp, text = hp, relief = tk.RAISED )
        self.hp_adjust_label.pack(side = tk.LEFT)
        """
        
        for parameter_list in self.list_of_parameters_right:
            exec("self.main_group_right_{0} = tk.Frame(self.main_group_right)". format(parameter_list))
            exec("self.main_group_right_{0}.pack(side = tk.BOTTOM)". format(parameter_list))
            exec("""self.{0}_adjust_label = tk.Label(self.main_group_right_{0}, text = "{0}: " )""". format(parameter_list))
            exec("self.{0}_adjust_label.pack(side = tk.LEFT, anchor = tk.E, fill=tk.BOTH)". format(parameter_list))
            exec("self.{0}_input_box = tk.Entry(self.main_group_right_{0})". format(parameter_list))
            exec("self.{0}_input_box.pack(side = tk.RIGHT, anchor = tk.E, fill=tk.BOTH)". format(parameter_list))
        

        self.root.mainloop()
# Start the application
def main():
    Application()

if __name__ == '__main__':
    main()


