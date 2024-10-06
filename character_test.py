from character import Enemy


dave = Enemy("Dave", "A smelly zombie")
dave.describe()

dave.set_conversation("Gaarrrhhhh, i'll eat your brains!!!")
dave.talk()
dave.set_weakness("cheese")

print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)
