import unittest
from threading import Thread

import time
import game_main as gm
import level_model as lm
import entity_data as ed
import entity_model as em
import interactive_model as im
import multiplayer_main as mm
import multiplayer_server as ms

###############################################################
# Main test file. Most of the code is moved into archives for #
# efficiency. All the test are commented out at the bottom of #
# This file.                                                  #
###############################################################


class TestGame(unittest.TestCase):
    def setUp(self):
        self.TestGame = gm.GameMain()
        self.TestGame.initialize_level('Level 1', 8, 8)
        self.TestGame.set_current_level('Level 1')

        self.DummyPC = em.PlayerModel(1, 1, 'PC1', 'RNGod', 'PC1', 'player', 16, 4, 4, 4, 4)
        self.DummyEnemy = em.EnemyModel(2, 1, ' g ', 'Goblin', 'gob001', 'enemy', 2, 2, 2, 2, 2)

        self.DummyDesk = im.ContainerModel(1, 2, ' D ', 'Desk', 'desk001', 'container')
        self.DummyDesk.set_container('Sword', 1)

    def setup_game(self):
        self.TestGame.position_entity(self.DummyPC)
        self.TestGame.position_entity(self.DummyDesk)
        self.TestGame.position_entity(self.DummyEnemy)

        level = self.TestGame.return_current_level()
        level.add_player(self.DummyPC)
        level.add_entity(self.DummyEnemy)
        level.add_interactive(self.DummyDesk)

    def test_return_levels(self):
        self.assertNotEqual(self.TestGame.return_levels(), {})

    def test_start_game(self):
        self.TestGame.start_game()

    """
    def test_sockets(self):
        option = self.TestGame.open_menu()
        if option == 'mp_ng':
            t1 = Thread(target=ms.start_server)
            t2 = Thread(target=mm.start_client, args=('Player1',))
            t1.start()
            t2.start()
    """


if __name__ == '__main__':
    unittest.main()


"""
        TEST ARCHIVES:
        
    #BLOCKED WHEN NOT IN USE#

    def test_open_menu(self):
        check_this = self.TestGame.open_menu()
        self.assertIsNotNone(check_this)
        
    def test_save_game(self):
        self.setup_game()
        self.TestGame.initialize_level('Level 2', 6, 6)
        self.TestGame.save_game('save_002')

    def test_load_game(self):
        levels = self.TestGame.load_game('save_002')
        self.assertIn('Level 1', levels)
    
    
        
    def test_initialize_level(self):
        levels = self.TestGame.return_levels()
        self.assertIn('Level 1', levels)
        self.assertIsInstance(levels.get('Level 1'), lm.LevelModel)

    def test_set_current_level(self):
        levels = self.TestGame.return_levels()
        self.assertEqual(levels.get('Level 1'), self.TestGame.return_current_level())

    def test_draw_map(self):
        check_this = self.TestGame.draw_map()
        self.assertIsInstance(check_this, str)

    def test_create_entity(self):
        new_entity = self.TestGame.create_entity(ed.goblin)
        self.assertIsInstance(new_entity, em.EnemyModel)

    def test_populate_map(self):
        self.TestGame.populate_map(ed.goblin, 0, 0)
        check_this = self.TestGame.return_current_level().return_entities()
        self.assertNotEqual(check_this[0].return_position(), (0, 0))
        level = self.TestGame.return_current_level()
        level.FOR_TEST_ONLY_set_structure()
        level.FOR_TEST_ONLY_set_cell_to(6, 5, '   ')
        self.TestGame.populate_map(ed.goblin, 0, 0)
        check_this = self.TestGame.return_current_level().return_entities()
        self.assertEqual(check_this[1].return_position(), (6, 5))

        OLD CODE ARCHIVES:
        
        OLD LOAD/SAVE GAME SKETCH. NO PICKLE.
        
            def test_load_game(self):
        self.TestGame.delete_levels()

        def trim_parameters(data):
            trimmed = list()
            for param in data:
                param = param.strip(" '[()]]' \n")
                trimmed.append(param)
            return trimmed

        with open('save_game.txt', 'r') as load_game:
            lines = load_game.readlines()
            level_setup = None
            for data in lines:
                data = data.split(',')
                if 'LEVEL' in data:
                    trim_data = trim_parameters(data)
                    new_level = self.TestGame.load_level(trim_data[1], int(trim_data[2]), int(trim_data[3]))
                    new_level.load_structure(trim_data[4:])
                    level_setup = new_level
                if 'PLAYER' in data:
                    trim_data = trim_parameters(data)
                    create_player = em.PlayerModel(int(trim_data[1]), int(trim_data[2]), trim_data[3], trim_data[4],
                                                   trim_data[5], trim_data[6], int(trim_data[7]), int(trim_data[8]),
                                                   int(trim_data[9]), int(trim_data[10]), int(trim_data[11]))
                    level_setup.add_player(create_player)
                if 'ENTITY' in data:
                    trim_data = trim_parameters(data)
                    create_entity = em.EnemyModel(int(trim_data[1]), int(trim_data[2]), trim_data[3],
                                                  trim_data[4], trim_data[5], trim_data[6],
                                                  int(trim_data[7]), int(trim_data[8]), int(trim_data[9]),
                                                  int(trim_data[10]), int(trim_data[11]))
                    level_setup.add_entity(create_entity)
                if 'INTERACTIVE' in data:
                        trim_data = trim_parameters(data)
                        if trim_data[6] == 'container':
                            create_container = im.ContainerModel(int(trim_data[1]), int(trim_data[2]), trim_data[3],
                                                                 trim_data[4], trim_data[5], trim_data[6])
                            level_setup.add_interactive(create_container)
            print(self.TestGame.draw_map())
            
        :: BLOCKED WHEN NOT IN USE ::
        Old save_game code sketch.
        
         def test_save_game(self):
        Full test for this code is at the bottom of this file in Code Archives.
        ### SET UP FOR TEST ###
        self.TestGame.initialize_level('Level 2', 8, 8)
        self.TestGame.initialize_level('Level 3', 8, 8)
        level = self.TestGame.return_current_level()
        self.TestGame.position_entity(self.DummyPC)
        level.add_player(self.DummyPC)

        ### SET UP ENEMY ###
        self.TestGame.position_entity(self.DummyEnemy)
        level.add_entity(self.DummyEnemy)

        ### SET UP DESK ###
        self.TestGame.position_entity(self.DummyDesk)
        level.add_interactive(self.DummyDesk)

        self.TestGame.save_game('save_001', self.TestGame.return_levels())
        
        ### SET UP FOR TEST ###
        self.TestGame.position_entity(self.DummyPC)
        self.TestGame.position_entity(self.DummyDesk)
        level = self.TestGame.return_current_level()
        check_this = level.return_cell_content(1, 1)
        self.assertEqual(check_this, self.DummyPC.return_map_model())

        ### SET UP ENEMY ###
        self.TestGame.position_entity(self.DummyEnemy)
        level.add_entity(self.DummyEnemy)

        ### SET UP DESK ###
        level.add_interactive(self.DummyDesk)

        print(self.TestGame.draw_map())

        # DIRTY CODE

        with open('save_game.txt', 'w') as save_game:
            data = self.DummyPC.return_data()
            save_game.write(f'{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]},'
                                f' {data[6]}, {data[7]}, {data[8]}, {data[9]}, {data[10]}, {data[11]},'
                                f' {data[12]},')
            save_game.write(' Inventory: ')
            for item in self.DummyPC.return_inventory():
                save_game.write(f'{item}, {self.DummyPC.return_inventory()[item]}')
            save_game.write(f', Equipment: {self.DummyPC.return_equipment()}')
            save_game.write(' \n')
            for entity in level.return_entities():
                data = entity.return_data()
                save_game.write(f'{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]},'
                                f' {data[6]}, {data[7]}, {data[8]}, {data[9]}, {data[10]}, {data[11]},'
                                f' {data[12]}, {data[13]} \n')
            for interactive in level.return_interactive():
                data = interactive.return_data()
                save_game.write(f'{data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}')
                save_game.write(', Contents: ')
                for item in interactive.return_container():
                    save_game.write(f'{item}, {interactive.return_container()[item]}')
                save_game.write(' \n')

        with open('save_game.txt', 'r') as load_game:
            data = load_game.readline()
            self.assertEqual(data, '(1, 1), PC1, RNGod, PC1, player, 16, 4, 4, 4, 4, 20, 40, 20, Inventory: , Equipment: ({}, {}) \n')
            data2 = load_game.readline()
            self.assertEqual(data2, '(2, 1),  g , Goblin, gob001, enemy, 2, 2, 2, 2, 2, 3, 20, 10, None \n')
            data3 = load_game.readline()
            self.assertEqual(data3, '(1, 2),  D , Desk, desk001, container, Contents: Sword, 1 \n')

        """
"""

    #BLOCKED WHEN NOT IN USE.

    def test_player_move(self):
        ### SET UP FOR TEST ###
        self.TestGame.position_entity(self.DummyPC)
        self.TestGame.position_entity(self.DummyDesk)
        level = self.TestGame.return_current_level()
        check_this = level.return_cell_content(1, 1)
        self.assertEqual(check_this, self.DummyPC.return_map_model())
        print(self.TestGame.draw_map())

        ### SET UP ENEMY ###
        self.TestGame.position_entity(self.DummyEnemy)
        self.TestGame.return_current_level().add_entity(self.DummyEnemy)

        ### SET UP DESK ###
        level.add_interactive(self.DummyDesk)

        ### TEST ###
        check_this = self.DummyPC.return_position()
        self.DummyPC.move_player()
        against_that = self.DummyPC.return_position()
        if level.if_cell_empty(against_that[0], against_that[1]):
            self.assertNotEqual(check_this, against_that)
            level.update_entity_pos(against_that[0], against_that[1], self.DummyPC.return_map_model())
            self.assertEqual(level.return_cell_content(against_that[0], against_that[1]), "PC1")
            """              """
            level.remove_entity(check_this[0], check_this[1], self.DummyPC.return_map_model())
            self.assertEqual(level.return_cell_content(check_this[0], check_this[1]), "   ")
        else:
            enemy = self.TestGame.check_enemies(against_that)
            if enemy:
                enemy.take_damage(self.DummyPC.return_atk())
                self.assertEqual(enemy.return_hp(), 0)
                if enemy.return_hp() == 0:
                    print(f'{enemy.return_name()} is dead.')
                    self.TestGame.kill_entity(enemy.return_position(), enemy)
                    self.TestGame.drop_loot(enemy.return_position(), self.DummyDesk)
            else:
                interactive = self.TestGame.check_interactive(against_that)
                if interactive:
                    self.TestGame.interaction(interactive, self.DummyPC)
                else:
                    print("I can't move there !")

        print(self.TestGame.draw_map())


    def test_open_menu(self):
        option = self.DummyPC.move_player()
        if option == "i":
            self.TestGame.open_menu(option)
        else:
            self.TestGame.open_menu("main")
    """