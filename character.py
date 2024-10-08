import random

class Character:
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def describe(self):
        print(f"{self.name} appear before you!")
        print(self.description)

    def set_conversation(self, conversation):
        self.conversation = conversation

    def talk(self):
        if self.conversation is not None:
            print(f"[{self.name}] says: {self.conversation}")
        else:
            print(f"{self.name} doesn't want to talk to you.")

    def fight(self, combat_item):
        print(f"{self.name} doesn't want to fight with you.")
        return True  # Default return for non-enemies

    def bribe(self, item):
        print(f"You offer {self.name} a {item}.")
        if item.lower() == "gold":
            print(f"{self.name} accepts the bribe, turns and walks away.")
            return True
        else:
            print(f"{self.name} laughs evilly and pulls out a weapon to attack!")
            return False


class Enemy(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    def fight(self, combat_item):
        if combat_item.lower() == self.weakness:
            print(f"You fend {self.name} off with the {combat_item}!")
            return True
        else:
            print(f"{self.name} crushes you, puny adventurer!")
            return False

    def steal(self):
        stolen_items = ["gold coin", "magic amulet", "dagger"]
        if random.choice([True, False]):
            stolen_item = random.choice(stolen_items)
            print(f"You successfully stole a {stolen_item} from {self.name}.")
            return stolen_item
        else:
            print(f"{self.name} caught you! Prepare for a fight!")
            return None

    def bribe(self, item):
        acceptable_items = ["gold", "precious stone", "magic scroll"]
        if item.lower() in acceptable_items:
            print(f"{self.name} accepts the bribe and leaves you alone.")
            return True
        else:
            print(f"{self.name} refuses the bribe and attacks!")
            return False


class Friend(Character):
    def elven_sign_of_friendship(self):
        print(f"{self.name} holds their hand to their heart and then out towards you and says 'Welcome, friend!'")

    def give_gift(self, gift):
        print(f"You give {self.name} a {gift}. They seem happy and wish you luck on your journey!")

    def wisdom(self):
        print("A rhythmic key sways to reveal the hidden door.")

    def potion(self):
        print("A purple sparkly magic potion that gives you another life")


class Player:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = []  # List to store inventory items

    def describe(self):
        print(f"{self.name} - {self.description}")

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"You picked up {item.name}.")

    def remove_from_inventory(self, item):
        self.inventory.remove(item)
        print(f"You dropped {item.name}.")

    def show_inventory(self):
        if self.inventory:
            print("In your bag you have:")
            for item in self.inventory:
                print(f"- {item.name}")
        else:
            print("A moth flies out from your bag when you open it. Your inventory is empty...")
