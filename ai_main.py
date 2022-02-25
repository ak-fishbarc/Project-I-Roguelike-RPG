import math


###################################################
# Pathfinding and in future hopefully cooperation #
# between brains' owners.                         #
###################################################

class Brain:
    def __init__(self):
        self.__owner = None
        self.__route = []

    def set_owner(self, entity: object):
        self.__owner = entity

    def return_owner(self) -> object:
        return self.__owner

    def return_route(self) -> list:
        return self.__route

    def if_path_clear(self, map_structure, start_x, start_y) -> bool:
        if map_structure[start_x][start_y] == "   ":
            return True
        else:
            return False

    ###################################################################
    # Simple code to evaluate if the route found by pathfinder can be #
    # shortened.                                                      #
    ###################################################################

    def evaluate_route(self, route, map_structure):
        route.reverse()
        pointer = route[0]
        evaluated_route = [pointer]
        ###################################################################
        # Run the route from B to A. Check if the next step in the route  #
        # is closer to A than current pointer. If it is, make new pointer #
        # out of step.                                                    #
        ###################################################################
        for step in route:
            if math.dist(step, route[-1]) < math.dist(pointer, route[-1]):
                pointer = step
                evaluated_route.append(pointer)

        ###########################################
        # Added only for illustration.            #
        ###########################################
        for step in evaluated_route:
            map_structure[step[0]][step[1]] = " x "
            self.draw_map(map_structure)

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

    ###############
    # Pathfinder. #
    ###############
    def find_path(self, map_structure, goal):

        clear_up = []
        start_x = self.__owner.return_position()[0]
        start_y = self.__owner.return_position()[1]
        current_path = [(start_x, start_y)]
        map_structure[start_x][start_y] = " x "
        while (start_x, start_y) != goal:
            self.draw_map(map_structure)
            try_pointer = self.move_pointer(map_structure, start_x, start_y)
            #############################################################################
            # If self.move_pointer returns different coordinates than it was given, add #
            # them to the path and update coordinates. Otherwise, it means that there's #
            # no path leading to the goal. Move back and check if there's any other way #
            # to get there.                                                             #
            #############################################################################
            if try_pointer != (start_x, start_y) and try_pointer not in current_path:
                current_path.append((start_x, start_y))
                start_x, start_y = try_pointer[0], try_pointer[1]
            else:
                clear_up.append((start_x, start_y))
                go_back = current_path.pop()
                start_x = go_back[0]
                start_y = go_back[1]

            map_structure[start_x][start_y] = " x "

            #######################################################################
            # Clear up the map and add new route for the brain's owner to follow. #
            #######################################################################
            if (start_x, start_y) == goal:
                print('Found it')
                for pos in clear_up:
                    map_structure[pos[0]][pos[1]] = "   "
                for pos in current_path:
                    map_structure[pos[0]][pos[1]] = "   "
                self.draw_map(map_structure)
                self.__route = current_path


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

    ##################################
    ##################################
    ##################################
