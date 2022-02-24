import ai_main as am
import entity_model as em
import unittest


class TestAI(unittest.TestCase):

    def setUp(self):
        self.new_brain = am.Brain()

        self.enemy = em.EnemyModel(5, 5, 'e', 'Enemy', 'enm001', 'enemy', 2, 3, 4, 5, 6)
        self.level = [['   ' for x in range(0, 8)] for y in range(0, 8)]

        self.new_brain.set_owner(self.enemy)

    def build_obstacles(self):
        for i in range(0, 7):
            self.level[0][i] = " # "
            self.level[7 - 1][i] = " # "
        for n in range(0, 7):
            self.level[n][0] = " # "
            self.level[n][7 - 1] = " # "
        for n in range(0, 4):
            self.level[n][3] = " # "
        self.level[4][4] = " # "
        self.level[4][3] = " # "

    def test_set_owner(self):
        self.assertIsNotNone(self.new_brain.return_owner())

    def test_if_path_clear(self):
        test_this = self.new_brain.if_path_clear(self.level, 1, 1)
        self.assertEqual(test_this, True)

    def test_move_pointer(self):
        test_this = self.new_brain.move_pointer(self.level, 1, 1)
        self.assertEqual(test_this, (0, 1))

    def test_find_path(self):
        self.build_obstacles()
        self.new_brain.find_path(self.level, (1, 1))



if __name__ == "__main__":
    unittest.main()
