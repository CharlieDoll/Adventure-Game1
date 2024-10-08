from room import Room
from character import Enemy, Character, Friend

# Setting up rooms
kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
dungeon = Room("Dungeon")
courtyard = Room("Courtyard")
pond = Room("Pond")

kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate decorations")
dungeon.set_description("A cold, dank room, filled with spider webs and rusty chains on teh walls.")
courtyard.set_description("A space fith stone floors, overgrown ivy, broken statues, a pond filled with water lillies and Gargoyles watching from the ramparts.")
pond.set_description("A beautiful pond, filled with water lillies that are in bloom and a fountain at the centre.")

# Linking rooms
kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")
dungeon.link_room(courtyard, "stairs")
courtyard.link_room(kitchen, "passageway")
pond.link_room(courtyard, "stone_pathway")

# Setting up characters
balor = Enemy("Balor the Mighty", "A smelly Ogre")
balor.set_conversation("I will eat you puny Adventurer!")
balor.set_weakness("mirror")
dining_hall.add_character(balor)

shadow_lord = Enemy("Shadow Lord", "A disciple of the arts!")
shadow_lord.set_conversation("Join me adventurer and help me unlock the power with they key!")
shadow_lord.set_weakness("fire")
ballroom.add_character(shadow_lord)

gargoyle = Enemy("Malevolent stone creature, whos goal is to steal the key for his master.")
gargoyle.set_conversation("You hear the flapping of wings")
balor.set_weakness("axe")
courtyard.add_character(gargoyle)

elf = Friend("Arrina", "A forest Elf")
elf.set_conversation("Hello Adventurer, may your quest be blessed by the Goddess")
dining_hall.add_character(elf)

gnome = Friend("Tarrin", "A friendly Gnome")
gnome.set_conversation("Hello Adventurer, may your quest be blessed by the Goddess")
kitchen.add_character(gnome)

water_sprite = Friend("A magical creature, that lives in the pond")
water_sprite.set_conversation("Welcome adventurer. Let us help you complete your quest.")
pond.add_character(water_sprite)

# Player character
player = Character("Our Adventurer", "A brave soul looking for treasure.")
player_inventory = []  # List to store player inventory

# Starting room
current_room = kitchen

while True:
    print("\n")
    current_room.get_details()

    characters_in_room = current_room.get_characters()
    items_in_room = current_room.get_items()

    # Only ask for a character once, if there are any
    if characters_in_room:
        print("Choose a character to interact with:")
        for i, character in enumerate(characters_in_room, start=1):
            print(f"{i}. {character.name}")
        char_choice = input("Enter the number of the character: ")

        if char_choice.isdigit() and 1 <= int(char_choice) <= len(characters_in_room):
            chosen_character = characters_in_room[int(char_choice) - 1]
            print(f"You have chosen to interact with {chosen_character.name}.")
        else:
            print("Invalid choice. Try again.")
            continue
    else:
        chosen_character = None

    while True:
        # Getting player command
        command = input("> ").lower()

        # Movement
        if command in ["north", "south", "east", "west", "stairs", "passageway", "stone_pathway"]:
            current_room = current_room.move(command)
            break  # Exit the inner loop to allow room change

        # Talk
        elif command == "talk" and chosen_character:
            print(f"You are talking to {chosen_character.name}")
            chosen_character.talk()

        # Pick up an item
        elif command == "pickup":
            if items_in_room:
                print("Choose an item to pick up:")
                for i, item in enumerate(items_in_room, start=1):
                    print(f"{i}. {item.name}")
                item_choice = input("Enter the number of the item: ")
                
                if item_choice.isdigit() and 1 <= int(item_choice) <= len(items_in_room):
                    chosen_item = items_in_room[int(item_choice) - 1]
                    player.add_to_inventory(chosen_item)
                    current_room.remove_item(chosen_item)
                else:
                    print("Invalid choice. Try again.")
            else:
                print("There are no items to pick up.")

        # Drop an item
        elif command == "drop":
            if player.inventory:
                print("Choose an item to drop:")
                for i, item in enumerate(player.inventory, start=1):
                    print(f"{i}. {item.name}")
                item_choice = input("Enter the number of the item: ")
                
                if item_choice.isdigit() and 1 <= int(item_choice) <= len(player.inventory):
                    chosen_item = player.inventory[int(item_choice) - 1]
                    player.remove_from_inventory(chosen_item)
                    current_room.add_item(chosen_item)
                else:
                    print("Invalid choice. Try again.")
            else:
                print("Your inventory is empty.")

        # Show inventory
        elif command == "inventory":
            player.show_inventory()

        # Quit the game
        elif command == "quit":
            print("Exiting the game. Goodbye!")
            exit()

        # Invalid command
        else:
            print("Invalid command. Try 'north', 'south', 'east', 'passageway', 'stone_pathway', 'talk', 'pickup', 'drop', 'inventory', or 'quit'.")
