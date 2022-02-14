import unittest
import entity_model as em

""" Test for entity model and methods """


class ItemDummy:
    def __init__(self, power, name):
        self.power = power
        self.name = name


class TestEntityM(unittest.TestCase):

    def setUp(self) -> None:
        self.TestGod = em.PlayerModel(3, 3, 'PC1', 'RNGod', 'RNGod', 'player', 4, 4, 4, 4, 4)
        self.DummySwrd = ItemDummy(3, "Dummy Sword")
        self.DummyAxe = ItemDummy(5, "Dummy Axe")

        self.TestEnemy = em.EnemyModel(5, 5, ' g ', 'Goblin', 'gob001', 'enemy', 1, 1, 1, 1, 1)

    def test_move_updown(self):
        self.TestGod.move_updown(-1)
        check_this = self.TestGod.return_position()
        self.assertEqual(check_this[0], 2)

    def test_move_leftright(self):
        self.TestGod.move_leftright(-2)
        check_this = self.TestGod.return_position()
        self.assertEqual(check_this[1], 1)

    def test_inventory(self):
        swrd = self.DummySwrd
        self.TestGod.pick_up_item(swrd.name, 1)
        self.assertIn(swrd.name, self.TestGod.return_inventory())
        self.TestGod.pick_up_item(swrd.name, 1)
        check_swords = self.TestGod.return_inventory()[swrd.name]
        self.assertEqual(check_swords, 2)
        self.TestGod.pick_up_item(self.DummyAxe.name, 1)
        check_axes = self.TestGod.return_inventory()[self.DummyAxe.name]
        self.assertEqual(check_axes, 1)

    def test_equip_weapon(self):
        swrd = self.DummySwrd
        self.TestGod.equip_weapon(swrd.name, swrd.power)
        check_this = self.TestGod.return_atk()
        self.assertEqual(check_this, 5)
        self.TestGod.pick_up_item(swrd.name, 1)
        self.TestGod.equip_weapon(swrd.name, swrd.power)
        check_that = self.TestGod.return_atk()
        self.assertEqual(check_that, 8)

    def test_change_weapon(self):
        swrd = self.DummySwrd
        axe = self.DummyAxe
        self.TestGod.pick_up_item(swrd.name, 1)
        self.TestGod.pick_up_item(axe.name, 1)
        self.TestGod.equip_weapon(swrd.name, swrd.power)
        self.assertEqual(self.TestGod.return_atk(), 8)
        self.TestGod.equip_weapon(axe.name, axe.power)
        self.assertEqual(self.TestGod.return_atk(), 10)

    def test_equip_armor(self):
        swrd = self.DummySwrd
        self.TestGod.equip_armor(swrd.name, swrd.power)
        check_this = self.TestGod.return_hp()
        self.assertEqual(check_this, 40)
        self.TestGod.pick_up_item(swrd.name, 1)
        self.TestGod.equip_armor(swrd.name, swrd.power)
        check_that = self.TestGod.return_hp()
        self.assertEqual(check_that, 43)

    def test_change_armor(self):
        swrd = self.DummySwrd
        axe = self.DummyAxe
        self.TestGod.pick_up_item(swrd.name, 1)
        self.TestGod.pick_up_item(axe.name, 1)
        self.TestGod.equip_armor(swrd.name, swrd.power)
        self.assertEqual(self.TestGod.return_hp(), 43)
        self.TestGod.equip_armor(axe.name, axe.power)
        self.assertEqual(self.TestGod.return_hp(), 45)

    def test_take_damage(self):
        check_that = self.TestGod.return_hp()
        self.TestGod.take_damage(self.TestEnemy.return_name(), self.TestEnemy.return_atk())
        against_that = self.TestGod.return_hp()
        self.assertNotEqual(check_that, against_that)

    def test_set_target(self):
        self.TestEnemy.set_target(self.TestGod)
        check_against = self.TestEnemy.return_target()
        self.assertEqual(self.TestGod, check_against)

    def test_search_for_target(self):
        self.TestEnemy.set_target(self.TestGod)
        self.TestEnemy.search_and_destroy()
        check_this = self.TestEnemy.return_position()
        against_that = self.TestGod.return_position()
        self.assertEqual(check_this, (4, 5))
        self.assertNotEqual(check_this, against_that)

    def test_enemy_attack(self):
        self.TestEnemy.set_target(self.TestGod)
        full_hp = self.TestGod.return_hp()
        while self.TestGod.return_hp() == full_hp:
            self.TestEnemy.search_and_destroy()
        self.assertNotEqual(self.TestGod.return_hp(), full_hp)

    def test_set_position(self):
        self.TestEnemy.set_positions(8, 8)
        check_this = self.TestEnemy.return_position()
        self.assertEqual(check_this, (8, 8))

    def test_set_id(self):
        self.TestEnemy.set_id('NewId')
        self.assertEqual(self.TestEnemy.return_id(), 'NewId')


if __name__ == "__main__":
    unittest.main()
