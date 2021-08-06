import random
names = ['Zolg', 'Dolg', 'Molg', 'Eruin', 'Meru', 'Sharu', 'Zonir']
titles = ['the Mad', 'the Black Hand', 'the Fury', 'the Pain']
classes = ['Mage', 'Warrior', 'General']


def name_generator():
    name_picked = random.choice(names)
    title_picked = random.choice(titles)
    return f"{name_picked} {title_picked}"


class Character:
    """Character attributes holder."""
    def __init__(self):
        self.name = name_generator()
        self.character_class = random.choice(classes)
        self.allegiance = "Mountain Lords"

    def description(self):
        print(f"| {self.name} swears allegiance to the {self.allegiance}. He is a {self.character_class}.")
        if "the Mad" in self.name:
            print("| His nickname is thanks to the brutal measures he takes against perceived dangers, no matter friend"
                  " or foe.")
        elif "the Black Hand" in self.name:
            print("| His nickname is because one of his hands leaks dark magic aura. No one knows why it is so.")
        elif "the Fury" in self.name:
            print("| His nickname is because he gives no mercy, and enters berserk rage when in battle.")
        elif "the Pain" in self.name:
            print("| His nickname comes from his sadistic nature to inflict pain upon his prisoners. Not a good idea to"
                  " surrender to such a man.")


class PlayerCharacter:
    """Player character class only."""
    def __init__(self, name, c):
        self.name = name
        self.character_class = c
        self.allegiance = "Rebels"

    def description(self):
        print(f"| {self.name} belongs to the {self.allegiance}. He is a {self.character_class}.")
        print(f"| He is the leader of his faction, is in war with the Mountain Lords, and is controlled by you :)")