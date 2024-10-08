from character import Character, Enemy, Friend

# Define the Player class with an inventory
class Player:
    def __init__(self):
        self.inventory = []

    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} added to your inventory.")

    def show_inventory(self):
        if self.inventory:
            print("You are carrying:")
            for item in self.inventory:
                print(f"- {item}")
        else:
            print("Your inventory is empty.")


# Create the player character
player = Player()

# Testing with Balor the Enemy
balor = Enemy("Balor", "A smelly Ogre")
balor.describe()
balor.set_weakness("mirror")
print("What will you fight with?")
fight_item = input()
if balor.fight(fight_item):
    print("You won the fight against Balor!")
else:
    print("You lost the fight against Balor the Mighty!")

# Steal from Balor
stolen_item = balor.steal()
if stolen_item:
    player.add_to_inventory(stolen_item)

# Show player's inventory
player.show_inventory()

# Bribe Balor
bribe_item = input("What will you bribe Balor the Mighty with? ")
balor.bribe(bribe_item)


# Create another enemy (Shadow Lord)
shadow_lord = Enemy("Shadow Lord", "A disciple of hell!")
shadow_lord.set_weakness("fire")
shadow_lord.describe()

# Prompt the user for the weapon to fight the Shadow Lord
weapon = input("What will you fight with against the Shadow Lord? ")
if shadow_lord.fight(weapon):
    print("You defeated the Shadow Lord!")
else:
    print("You were defeated by the Shadow Lord!")

# Attempt to steal from SL
print("\nAttempting to steal from the Shadow Lord...")
shadow_lord.steal()

# Try to bribe the SL
print("\nAttempting to bribe the Shadow Lord...")
bribe_item = input("What will you bribe with? ")
shadow_lord.bribe(bribe_item)

# Create a friendly character (Arrina the Elf)
elf = Friend("Arrina", "A forest Elf")
elf.describe()
elf.talk()
elf.elven_sign_of_friendship()
elf.give_gift("magic potion")

# Create a Gnome friend character 

gnome = Friend("Tarrin", "A friendly Gnome")
gnome.describe()
gnome.talk()
gnome.wisdom()
gnome.give_gift("jewel")

# Create a Water Sprite Friend Character

water_sprite = Friend("Serena", "A water srite from the Lilly Pond")
water_sprite.describe()
water_sprite.talk()
water_sprite.potion("A glass potion vile, filled with a purple sparkly liquid")

# Show player's inventory after interacting with everyone
player.show_inventory()
