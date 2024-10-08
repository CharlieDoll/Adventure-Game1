class Room:
    def __init__(self, name):
        self.name = name
        self.description = None
        self.linked_rooms = {}
        self.characters = []  # List to store multiple characters
        self.items = []  # List to store items in the room

    def set_description(self, description):
        self.description = description

    def add_character(self, character):
        self.characters.append(character)  # Add character to the room

    def remove_character(self, character):
        self.characters.remove(character)  # Remove character from the room

    def add_item(self, item):
        self.items.append(item)  # Add item to the room

    def remove_item(self, item):
        self.items.remove(item)  # Remove item from the room

    def get_items(self):
        return self.items  # Return the list of items

    def describe_items(self):
        if self.items:
            print("You see the following items:")
            for item in self.items:
                print(f"- {item.name}")
        else:
            print("There are no items here.")

    def get_details(self):
        print(f"{self.name}")
        print("--------------------")
        print(self.description)
        if self.characters:
            print("Inhabitants in the room:")
            for character in self.characters:
                print(f"{character.name} - {character.description}")
        self.describe_items()  # List items in the room
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.name} is {direction}")
