class Item:
    def __init__(self, name):
        self.name = name
        self.description = None

    def get_name(self):
        return self.name

    def set_name(self, item_name):
        self.name = item_name

    def get_description(self):
        return self.description

    def set_description(self, item_description):
        self.description = item_description

    def describe(self):
        print(f"{self.name}: {self.description}")
            
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def describe(self):
        print(f"{self.name}: {self.description}")



# Adding the key as an item
key = Item("key")
key.set_description("A small golden key.")  # Using the setter method

# Lock mechanism for a room
class Room:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_rooms = {}
        self.inhabitant = None
        self.item = None
        self.is_locked = False  # Initial state: room is unlocked

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description

    def set_character(self, character):
        self.inhabitant = character

    def get_character(self):
        return self.inhabitant

    def set_item(self, item):
        self.item = item

    def get_item(self):
        return self.item

    def lock(self):
        self.is_locked = True
        print(f"The {self.name} is now locked.")

    def unlock(self, item):
        if item.get_name() == "key":
            self.is_locked = False
            print("The door unlocks!")
        else:
            print("This item can't unlock the door.")

    def link_room(self, room, direction):
        self.linked_rooms[direction] = room

    def move(self, direction):
        if direction in self.linked_rooms:
            next_room = self.linked_rooms[direction]
            if next_room.is_locked:
                print(f"The {next_room.name} is locked. You need a key to enter.")
                return self
            return next_room
        else:
            print("You can't go that way.")
            return self

    def get_details(self):
        print(f"{self.name}")
        print("--------------------")
        print(self.description)
        if self.is_locked:
            print("The room is locked.")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.name} is {direction}")
        if self.item:
            print(f"There is a {self.item.get_name()} in the room.")


# Create the rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
dungeon = Room("Dungeon")
courtyard = Room("Courtyard")
pond = Room("Pond")

# Set room descriptions
kitchen.set_description("A dank and dirty room buzzing with flies.")
ballroom.set_description("A vast room with a shiny wooden floor.")
dining_hall.set_description("A large room with ornate decorations.")
dungeon.set_description("A cold, dank room, filled with spider webs and rusty chains on teh walls.")
courtyard.set_description("A space fith stone floors, overgrown ovy and broken statues, with Gargoyles watching from teh ramparts.")
pond.set_description("A beautiful pond, filled with water lillies that are in bloom and a fountain at the centre.")

# Link rooms together
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
dungeon.link_room(courtyard, "stairs")
courtyard.link_room(kitchen, "passageway")
pond.link_room(courtyard, "stone_pathway")

# Add key to the ballroom
ballroom.set_item(key)

# Main game loop (example of using an item to unlock a room)
current_room = kitchen
player_inventory = [key]  # Player starts with the key in inventory

# Unlock the ballroom with the key
command = input("Do you want to use an item? (yes/no) ").lower()
if command == "yes":
    item_name = input("What do you want to use? ").lower()

    # Check if the item is in the inventory
    for item in player_inventory:
        if item.get_name() == item_name:
            ballroom.unlock(item)
            break
    else:
        print("You don't have that item.")
