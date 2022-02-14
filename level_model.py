""" Model for levels """


class LevelModel:

    def __init__(self, name: str, width: int, height: int):
        self.__name = name
        self.__w = width
        self.__h = height
        self.__structure = [["   " for n in range(self.__w)]
                            for i in range(self.__h)]
        self.__players = []
        self.__entities = []
        self.__interactive = []

    def FOR_TEST_ONLY_set_structure(self):
        self.__structure = [[" # " for n in range(self.__w)]
                            for i in range(self.__h)]

    def FOR_TEST_ONLY_set_cell_to(self, posx: int, posy: int, what: str):
        self.__structure[posx][posy] = what

    ##########################################################
    # Basic functions                                        #
    ##########################################################
    def return_structure(self):
        return self.__structure

    def return_dimensions(self):
        return (self.__w, self.__h)

    def return_players(self) -> list:
        return self.__players

    def return_entities(self) -> list:
        return self.__entities

    def return_interactive(self) -> list:
        return self.__interactive

    def return_name(self) -> str:
        return self.__name

    def add_player(self, player: object):
        self.__players.append(player)

    def add_entity(self, entity: object):
        self.__entities.append(entity)

    def add_interactive(self, thing: object):
        self.__interactive.append(thing)

    def return_cell_content(self, posx: int, posy: int):
        return self.__structure[posx][posy]

    def update_entity_pos(self, posx: int, posy: int, entity: str):
        self.__structure[posx][posy] = entity

    def remove_entity(self, posx: int, posy: int, entity: str):
        if self.__structure[posx][posy] == entity:
            self.__structure[posx][posy] = "   "

    #######################################
    # create_borders creates walls around #
    # the map.                            #
    #######################################

    def create_borders(self):
        for i in range(0, self.__w):
            self.__structure[0][i] = " # "
            self.__structure[self.__h-1][i] = " # "
        for n in range(0, self.__h):
            self.__structure[n][0] = " # "
            self.__structure[n][self.__w-1] = " # "

    #################################################
    # Returns map_model for print.                  #
    #################################################

    def print_map_model(self) -> str:
        map_model = ""
        for i in self.__structure:
            for n in i:
                map_model += n
            map_model += "\n" \

        return map_model

    def if_cell_empty(self, posx: int, posy: int) -> bool:
        if self.__structure[posx][posy] == "   ":
            return True
        else:
            return False

    #####################################################
    # load_structure used in old implementation of load #
    # game function.                                    #
    #####################################################

    def load_structure(self, data):
        inc = 0
        for i in range(self.__h):
            for n in range(self.__w):
                if len(data[inc]) < 2:
                    self.__structure[n][i] = f' {data[inc]} '
                else:
                    self.__structure[n][i] = f'{data[inc]}'
                inc += 1