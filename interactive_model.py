""" Models for interactive objects, containers, NPCs, etc."""


class InteractiveModel:
    def __init__(self, posx, posy, map_model, name, thing_id, kind):
        self.__px = posx
        self.__py = posy
        self.__map_model = map_model
        self.__name = name
        self.__thing_id = thing_id
        self.__kind = kind

    def return_data(self):
        return (self.return_position(), self.return_map_model(), self.return_name(), self.__thing_id, self.return_kind())

    def return_position(self) -> tuple:
        return (self.__px, self.__py)

    def return_name(self) -> str:
        return self.__name

    def return_map_model(self) -> str:
        return self.__map_model

    def return_kind(self) -> str:
        return self.__kind


class ContainerModel(InteractiveModel):
    def __init__(self, posx: int, posy: int, name: str, thing_id: str, map_model: str, kind: str):
        super().__init__(posx, posy, name, thing_id, map_model, kind)

        self.container = {}

    def return_container(self) -> dict:
        return self.container

    def set_container(self, name: str, amount: int):
        self.container[name] = amount

    def remove_from_container(self, name: str):
        self.container.pop(name)
