class ItemModel:
    def __init__(self, name: str, power: int, item_id):
        self.__name = name
        self.__power = power
        self.__item_id = item_id


"""

Obsolete Code - No Longer in Use

class LootBag:

    def __init__(self, posx, posy, map_model, bag_id):
        self.__px = posx
        self.__py = posy
        self.__map_model = map_model
        self.__bag_id = bag_id

        self.__contents = {}

    def return_contents(self) -> dict:
        return self.__contents

    def set_contents(self, name: str, amount: int):
        self.__contents[name] = amount
        
"""