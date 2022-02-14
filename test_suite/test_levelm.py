import level_model as lm
import unittest


class TestDummy:
    def __init__(self, posx, posy, name, map_model):
        self.px = posx
        self.py = posy
        self.name = name
        self.map_model = map_model


class TestLevelM(unittest.TestCase):

    def setUp(self) -> None:
        self.level001 = lm.LevelModel('Level 1', 8, 8)
        self.level001.create_borders()

        self.dummy01 = TestDummy(3, 3, "Dummy", ' D ')
        self.dumx = self.dummy01.px
        self.dumy = self.dummy01.py
        self.level001.update_entity_pos(self.dumx, self.dumy, self.dummy01.map_model)

    def test_return_name(self):
        self.assertEqual(self.level001.return_name(), 'Level 1')

    def test_add_entity(self):
        self.level001.add_entity(self.dummy01)
        check_this = self.level001.return_entities()[0]
        self.assertEqual(check_this, self.dummy01)

    def test_if_cell_empty(self):
        check_this = self.level001.if_cell_empty(2, 2)
        self.assertEqual(check_this, True)

    def test_update_entity(self):
        check_this = self.level001.return_cell_content(self.dumx, self.dumy)
        against_this = self.level001.return_cell_content(self.dumx, self.dumy)
        self.assertEqual(check_this, against_this)

    def test_remove_entity(self):
        check_this = self.level001.return_cell_content(3, 3)
        self.assertEqual(check_this, self.dummy01.map_model)
        self.level001.remove_entity(self.dumx, self.dumy, self.dummy01.map_model)
        check_that = self.level001.if_cell_empty(self.dumx, self.dumy)
        self.assertEqual(check_that, True)


if __name__ == "__main__":
    unittest.main()
