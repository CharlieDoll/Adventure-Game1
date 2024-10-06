from room import Room
# from character import Character
from character import Enemy
from character import Character



kitchen = Room("Kitchen")
ballroom = Room("Ballroom")
dining_hall = Room("Dining Hall")
# basement = Room("Basement")
# bathroom = Room("Bathroom")
# bedroom = Room("Bedroom")
# hallway = Room("Hallway")
# living_room = Room("Room")

kitchen.set_description("A dank and dirty room buzzing with flies")
ballroom.set_description("A vast room with a shiny wooden floor")
dining_hall.set_description("A large room with ornate decorations")
# basement.set_description("A dank, cold, wet space, full of junk, spider webs and zombies")
# bathroom.set_description("A cat jumps out at you")
# bedroom.set_description("Everything is covered in dust sheets and you notice that the wardrobes are still full of clothes")
# living_room.set_description("A large room with mouldy settees and water damage can be seen ")
# hallway.set_description("You walk in to teh hallway and climb a set of creaky stairs to the 2nd floor")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")
# basement.link_room(kitchen, "north")
# living_room.link_room(kitchen, "south")
# bathroom.link_room(bedroom, "west")
# hallway.link_room(living_room, "south")


dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("Brrlgrh... rgrhl... brains...")
dave.set_weakness("cheese")
dining_hall.set_character(dave)


player = Character("Our Adventurer")
player.set_conversation("I am here to find the golden key!")
player.set_weakness("sword")





current_room = kitchen
while True:
      print("\n")
      current_room.get_details()
      inhabitant = current_room.get_character()
      if inhabitant is not None:
            inhabitant.describe()


      command = input("> ")
      current_room = current_room.move(command)


      command = input("> ")
# Check whether a direction was typed
      if command in ["north", "south", "east", "west"]:
       current_room = current_room.move(command)
      elif command == "talk":

       while True:
        command = input("> ").lower()  # Convert input to lowercase to handle case insensitivity

    # Check whether a direction was typed
      if command in ["north", "south", "east", "west"]:
        current_room = current_room.move(command)
      elif command == "talk":
        # Method to interact with characters in the room
        current_room.talk_to_npc()
      elif command == "look":
        # Method to look around the room
        current_room.look_around()
      elif command == "inventory":
        # Player object with an inventory attribute
        player.show_inventory()
      elif command == "quit":
        print("Exiting the game. Goodbye!")
        break
      else:
        print("Invalid command. Try 'north', 'south', 'east', 'west', 'talk', 'look', 'inventory', or 'quit'.")
