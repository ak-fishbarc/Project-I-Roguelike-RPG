class Brain:
    def __init__(self):
        self.__owner = None

    def set_owner(self, entity: object):
        self.__owner = entity

    def return_owner(self) -> object:
        return self.__owner

    def if_path_clear(self, map_structure, start_x, start_y) -> bool:
        if map_structure[start_x][start_y] == "   ":
            return True
        else:
            return False

    def move_pointer(self, map_structure, start_x, start_y):
        if self.if_path_clear(map_structure, start_x - 1, start_y):
            start_x -= 1
        elif self.if_path_clear(map_structure, start_x, start_y - 1):
            start_y -= 1
        elif self.if_path_clear(map_structure, start_x + 1, start_y):
            start_x += 1
        elif self.if_path_clear(map_structure, start_x, start_y + 1):
            start_y += 1
        return (start_x, start_y)

    def find_path(self, map_structure, goal):

        current_path = []
        start_x = self.__owner.return_position()[0]
        start_y = self.__owner.return_position()[1]
        current_path.append((start_x, start_y))

        while (start_x, start_y) != goal:
            self.draw_map(map_structure)
            try_pointer = self.move_pointer(map_structure, start_x, start_y)
            if try_pointer not in current_path:
                current_path.append((start_x, start_y))
                start_x, start_y = try_pointer[0], try_pointer[1]
            else:
                n = 1
                while try_pointer in current_path:
                    start_x = current_path[0-n][0]
                    start_y = current_path[0-n][1]
                    try_pointer = self.move_pointer(map_structure, start_x, start_y)
                    n += 1

            map_structure[start_x][start_y] = " x "

            if (start_x, start_y) == goal:
                print('Found it')

    ##################################
    # Only for illustration purpose  #
    ##################################
    def draw_map(self, map_structure):
        draw = ""
        for x in map_structure:
            for y in x:
                draw += y
            draw += "\n"
        print(draw)
        draw = ""
    ##################################
    ##################################
    ##################################
