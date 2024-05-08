import art
import random


class Decider:

    def __init__(self):
        print(art.logo)
        self.names = ""
        self.name_list = []
        self.chosen_name = ""

    # start game printing logo and asking for the participants names as input, then turning it to a list #
    def gamestart(self):
        print(art.logo)
        self.names = input("Write down below the names of everyone who's participating of the game \n"
                           "separating each name with a comma, like this: Gabriel, Angelica, Andressa\n")
        self.name_list = self.names.split(", ")

    # pick a random name from the list #
    def pick_random_name(self):
        self.chosen_name = random.choice(self.name_list)

    # revealing the chosen name #
    def reveal_name(self):
        print(f"The one who's gonna pay tonight is......{self.chosen_name}")



