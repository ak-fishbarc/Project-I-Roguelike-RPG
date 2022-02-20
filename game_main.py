""" IMPORTS """
#####################
# Game-file Imports #
#####################

import entity_data as ed
import entity_model as em
import level_model as lm
import interactive_model as im

#################
# Other Imports #
#################

import pickle
import os
from random import randint

""" GAME'S CORE """

###########################################################
# self.__levels is a dictionary containing all the levels #
# created during the game.                                #
# self.__current_level defines level that is currently    #
# running.                                                #
# self.__dead_entities is a dictionary of dead entities   #
# that can be reused, instead of creating new objects and #
# using up the memory.                                    #
###########################################################

class GameMain:
    def __init__(self):
        self.__levels = {}
        self.__current_level = None
        self.__dead_entities = {}
        self.__running = False

    #############################
    # Basic operation functions #
    #############################
    def run(self):
        self.__running = True

    def pause(self):
        self.__running = False

    def delete_levels(self):
        self.__levels = {}

    def return_run(self):
        return self.__running

    def return_levels(self) -> dict:
        return self.__levels

    def return_current_level(self) -> object:
        return self.__current_level

    #############################################
    # open_menu and open_ingame_menu functions. #
    # Separated for clarity.                    #
    # Return choice as an option for            #
    # further processing.                       #
    #############################################

    def open_menu(self) -> str:
        greeting = "Welcome to Generic RPG game. \n \
Type: \n \
-> 'ng' for New Game. \n \
-> 'mp' for Multiplayer Game. \n \
-> 'load' to load a saved game."
        valid_choices = ['ng', 'mp', 'load']
        print(greeting)
        choice = input('')
        if choice.lower() in valid_choices:
            if choice.lower() == 'mp':
                option = input('Type New Game to start server or Join to join a server \n')
                if option == 'New Game':
                    return 'mp_ng'
            else:
                return choice

    def open_ingame_menu(self) -> str:
        greeting = """Type: \n \
-> 'lg' to Leave the Game. \n \
-> 'save' to Save the Game \n \
-> 'load' to Load the Game"""
        print(greeting)
        valid_choices = ['lg', 'save', 'load']
        choice = input('')
        if choice.lower() in valid_choices:
            return choice
        else:
            print('Option not recognized')

    ##################################################
    # Level related functions                        #
    ##################################################
    # initialize_level creates new level and adds it #
    # to list of levels in game.                     #
    # set_current_level defines which level is       #
    # currently running. Where the player is.        #
    ##################################################

    def initialize_level(self, name: str, width: int, height: int):
        nmp = lm.LevelModel(name, width, height)
        nmp.create_borders()
        self.__levels[nmp.return_name()] = nmp
        return nmp

    def set_current_level(self, name: str):
        if name in self.__levels:
            self.__current_level = self.__levels[name]
        else:
            print('There is a problem: Missing Level.')

    def draw_map(self) -> str:
        return self.__current_level.print_map_model()

    #########################################################
    # Objects related functions                             #
    #########################################################
    # create_entity creates an entity from a dictionary     #
    # it can use entity_data.py, ready made monsters or     #
    # could be used to make custom made monsters for        #
    # example, if in the future game editor would be        #
    # implemented.                                           #
    #########################################################

    def create_entity(self, data: dict) -> object:
        new_entity = em.EnemyModel(data['posx'], data['posy'], data['map_model'], data['name'],
                                   data['ent_id'], data['kind'], data['might'], data['swift'], data['life'],
                                   data['spirit'], data['mind'])
        return new_entity

    def create_player(self) -> object:
        new_player = em.PlayerModel(1, 1, ' P ', 'PC1', 'pc1', 'player', 6, 6, 6, 6, 6)

        return new_player
    #################################################################
    # populate_map can create new entity and look for an empty      #
    # random position on the map.                                   #
    # It is setting entity's position to new values and then adds   #
    # it to the level's entities list. It does not physically place #
    # entity in the level's structure. Use position_entity for that.#
    #################################################################

    def populate_map(self, entity_data: dict, posx: int, posy: int):
        new_entity = self.create_entity(entity_data)
        if posx == 0 and posy == 0:
            while posx == 0 and posy == 0:
                posx = randint(1,7)
                posy = randint(1,7)
                if self.__current_level.if_cell_empty(posx, posy):
                    new_entity.set_positions(posx, posy)
                else:
                    posx = 0
                    posy = 0
        else:
            if self.__current_level.if_cell_empty(posx, posy):
                new_entity.set_positions(posx, posy)

        self.__current_level.add_entity(new_entity)

    #############################################################
    # position_entity places entity in the level's structure    #
    # using entity's position attributes.                       #
    #############################################################

    def position_entity(self, entity: object):
        positions = entity.return_position()
        self.__current_level.update_entity_pos(positions[0], positions[1], entity.return_map_model())

    def kill_entity(self, where: tuple, entity: str):
        self.__current_level.remove_entity(where[0], where[1], entity.return_map_model())
        self.__dead_entities[entity.return_name()] = entity

    def drop_loot(self, where: tuple, what: object):
        self.__current_level.update_entity_pos(where[0], where[1], what.return_map_model())
        self.__current_level.add_interactive(what)

    #############################################################
    # Map check functions used for collisions and interactions. #
    #############################################################

    def check_enemies(self, position: tuple):
        enemies = self.__current_level.return_entities()
        for enemy in enemies:
            if enemy.return_position() == position:
                return enemy
            else:
                return False

    def check_interactive(self, position):
        interactives = self.__current_level.return_interactive()
        for active in interactives:
            if active.return_position() == position:
                return active
            else:
                return False

    ################################################################
    # Interaction function                                         #
    ################################################################
    # At the moment the only use for this function is to recognize #
    # if an object is a container and if it has any items to       #
    # collect.                                                     #
    # In future it could start a chat with NPC etc.                #
    ################################################################

    def interaction(self, interactive: object, interacting: object):
        if interactive.return_kind() == "container":
            items = interactive.return_container()
            for item in items:
                print(f"There is {items[item]} {item} inside {interactive.return_name()}")
                choice = input("Would you like to pick it up ?")
                if choice.lower() == "y":
                    interacting.pick_up_item(item, items[item])
                    interactive.remove_from_container(item)
                else:
                    continue

    #########################################################
    # save_game and load_game functions using.              #
    #########################################################
    # Currently game uses simple pickle into text file way  #
    # of saving and loading data.                           #
    #########################################################

    def load_level(self, name: str, width: int, height: int):
        load_level = lm.LevelModel(name, width, height)
        self.__levels[name] = load_level
        return load_level

    def save_game(self, save_name: str):
        with open(f'{save_name}.txt', 'wb') as save_file:
            for level in self.__levels:
                pickle.dump(self.__levels[level], save_file)

    def load_game(self, save_name: str) -> dict:
        levels = {}
        end_of_file = os.path.getsize(f'{save_name}.txt')

        with open(f'{save_name}.txt', 'rb') as load_file:
            while load_file.tell() != end_of_file:
                level = pickle.load(load_file)
                levels[level.return_name()] = level
        return levels

    ###########################################################
    # start_game function. Currently in progress.             #
    ###########################################################
    # Below if __name__ == '__main__' there are old pieces of #
    # code used in creation of this project.                  #
    ###########################################################

    def start_game(self):
        level = self.initialize_level('Level 001', 8, 8)
        self.set_current_level(level.return_name())
        self.populate_map(ed.goblin, 0, 0)
        place_entities = self.__current_level.return_entities()
        for entity in place_entities:
            self.position_entity(entity)
        single_player = self.create_player()
        self.__current_level.add_player(single_player)
        self.position_entity(single_player)
        print(self.draw_map())
        self.run()

    def player_move(self):
        player = self.__current_level.return_players()[0]
        pcords = player.return_position()
        player.move_player()
        new_cords = player.return_position()
        if self.__current_level.if_cell_empty(new_cords[0], new_cords[1]):
            self.__current_level.remove_entity(pcords[0], pcords[1], player.return_map_model())
            self.position_entity(player)
        else:
            player.set_positions(pcords[0], pcords[1])

    def turn(self):
        self.player_move()
        print(self.draw_map())


if __name__ == '__main__':
    pass


""" 
     OLD CODE ARCHIVES:
     
     SAVE/LOAD GAME USING TXT FILE. NO PICKLE.
     
     def load_game(self, save_name: str):
        self.__levels = {}
        data = []

        def trim_parameters(data):
            trimmed = list()
            for param in data:
                param = param.strip(" '[()]]' \n")
                trimmed.append(param)
            return trimmed

        with open(f'{save_name}.txt', 'r') as load_game:
            lines = load_game.readlines()
            level_setup = None
            for data in lines:
                data = data.split(',')
                if 'LEVEL' in data:
                    trim_data = trim_parameters(data)
                    new_level = self.load_level(trim_data[1], int(trim_data[2]), int(trim_data[3]))
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


     def save_game(self, save_name: str, levels: dict):
        with open(f'{save_name}.txt', 'w') as save_game:

            for level in levels:
                level = levels[level]
                save_game.write(f'LEVEL, {level.return_name()}, {level.return_dimensions()}, {level.return_structure()} \n')
                for player in level.return_players():
                    data = player.return_data()
                    save_game.write(f'PLAYER, {data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]},'
                                    f' {data[6]}, {data[7]}, {data[8]}, {data[9]}, {data[10]}, {data[11]},'
                                    f' {data[12]},')
                    save_game.write(' Inventory, ')
                    for item in player.return_inventory():
                        save_game.write(f'{item}, {player.return_inventory()[item]}')
                    save_game.write(f', Equipment, {player.return_equipment()}')
                    save_game.write(' \n')
                for entity in level.return_entities():
                    data = entity.return_data()
                    save_game.write(f'ENTITY, {data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]},'
                                    f' {data[6]}, {data[7]}, {data[8]}, {data[9]}, {data[10]}, {data[11]},'
                                    f' {data[12]}, {data[13]} \n')

                for interactive in level.return_interactive():
                    data = interactive.return_data()
                    save_game.write(f'INTERACTIVE, {data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}')
                    save_game.write(', Contents, ')
                    for item in interactive.return_container():
                        save_game.write(f'{item}, {interactive.return_container()[item]}')
                save_game.write('\n END LEVEL \n')

"""