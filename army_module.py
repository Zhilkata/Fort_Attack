from random import randint


class Army:
    """Army class holder."""

    def __init__(self, ri, ei, hi, c, m, s, a, character):
        self.regular_infantry = ri
        self.elite_infantry = ei
        self.heavy_infantry = hi
        self.cavalry = c
        self.mages = m
        self.sappers = s
        self.archers = a
        self.level = self.army_level()
        self.morale_modifier = self.morale_buff()
        self.morale = 100

        self.captain_object = character
        self.captain = character.name
        self.faction = character.allegiance

        self.intel_gathered = 0

    def report(self):
        print("==========Army Info==========")
        print(f"| Regular infantry: {self.regular_infantry}")
        print(f"| Elite infantry: {self.elite_infantry}")
        print(f"| Heavy infantry: {self.heavy_infantry}")
        print(f"| Cavalry: {self.cavalry}")
        print(f"| Mages: {self.mages}")
        print(f"| Sappers: {self.sappers}")
        print(f"| Archers: {self.archers}")
        print("/===========================/")
        print(f"+ Army level: {self.level}")
        print(f"+ Army morale: {self.morale}%")
        print("\n")

    def army_level(self):
        max_level_quota = 15000*1 + 250*5 + 1500*4 + 5000*2 + 5*7 + 150*6 + 6000*3
        army_level_quota = self.regular_infantry*1 + self.elite_infantry*5 + self.heavy_infantry*4 + self.cavalry*2 +\
                           self.mages*7 + self.sappers*6 + self.archers*3
        army_level = army_level_quota / max_level_quota
        if 1 >= army_level > 0.75:
            return "Legendary Host"
        elif 0.75 >= army_level > 0.50:
            return "Formidable"
        elif 0.50 >= army_level > 0.25:
            return "Regular"
        else:
            return "Poor"

    def morale_buff(self):
        if self.level == "Poor":
            return 1
        elif self.level == "Regular":
            return 2
        elif self.level == "Formidable":
            return 3
        elif self.level == "Legendary Host":
            return 5

    def captain_info(self):
        print("==========Captain Info==========")
        print(f"| Name: {self.captain}")
        print(f"| Allegiance: {self.faction}")
        if self.intel_gathered == 1 or self.captain == "Bolg the Usurper":
            self.captain_object.description()
        elif self.intel_gathered == 0:
            print("| No further info available.")
        print("\n")