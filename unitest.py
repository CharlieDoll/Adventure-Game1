import unittest
from character import Character, Enemy, Friend



class TestCharacter(unittest.TestCase):
    def test_character_talk(self):
        character = Character("Test Character")
        self.assertEqual(character.name, "Test Character")
        character.talk()

    def test_enemy_fight(self):
        enemy = Enemy("Shadow Lord", "A disciple of Hell!")
        result = enemy.fight("shadow magic")
        self.assertTrue(result)

    def test_friend_elven_sign_of_friendship(self):
        friend = Friend("Arrina", "A forest Elf")
        friend.elven_sign_of_friendship()

if __name__ == '__main__':
    unittest.main()