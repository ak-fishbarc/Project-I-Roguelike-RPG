from math import ceil, floor

""" Player and enemy models """


class EntityModel:
    def __init__(self, posx: int, posy: int, map_model: str, name: str, ent_id: str, kind: str):
        self.__px = posx
        self.__py = posy
        self.__map_model = map_model
        self.__name = name
        self.__my_id = ent_id
        self.__kind = kind

    def return_map_model(self) -> str:
        return self.__map_model

    def return_position(self) -> tuple:
        coordinates = (self.__px, self.__py)
        return coordinates

    def set_positions(self, posx: int, posy: int):
        self.__px = posx
        self.__py = posy

    def return_id(self) -> str:
        return self.__my_id

    def set_id(self, my_id: str):
        self.__my_id = my_id

    def return_kind(self) -> str:
        return self.__kind

    def move_updown(self, num: int):
        self.__px += num

    def move_leftright(self, num: int):
        self.__py += num

    def return_name(self) -> str:
        return self.__name


class PlayerModel(EntityModel):

    def __init__(self, posx: int, posy: int, map_model: str, name: str, ent_id: str, kind: str,
                 might: int, swift: int, life: int, spirit: int, mind: int):
        super().__init__(posx, posy, map_model, name, ent_id, kind)

        self.__might = might
        self.__swift = swift
        self.__life = life
        self.__spirit = spirit
        self.__mind = mind
        self.__atk = ceil(might * 1.25)
        self.__hp = floor(life * 10)
        self.__mana = floor(spirit * 5)

        self.__inventory = {}
        self.__weapon_slot = {}
        self.__armor_slot = {}

    def return_data(self):
        return (super().return_position(), super().return_map_model(), super().return_name(),
                super().return_id(), super().return_kind(), self.__might, self.__swift, self.__life,
                self.__spirit, self.__mind, self.__atk, self.__hp, self.__mana)

    def return_equipment(self):
        return (self.__weapon_slot, self.__armor_slot)

    def return_inventory(self) -> dict:
        return self.__inventory

    def return_atk(self) -> int:
        return self.__atk

    def return_hp(self) -> int:
        return self.__hp

    def take_damage(self, source: str, dmg: int):
        self.__hp -= dmg
        print(f"You have taken {dmg} damage from {source}.")
        print(f"You have {self.__hp}hp left.")

    def pick_up_item(self, name: str, amount: int):
        if name not in self.__inventory:
            self.__inventory[name] = amount
        else:
            self.__inventory[name] += amount
        print(f"You have picked up {amount} {name}.")

    def equip_weapon(self, name: str, power: int):
        if name in self.__inventory and self.__weapon_slot == {}:
            self.__weapon_slot[name] = power
            self.__atk += power
            print(f"You have now equipped {name} as a weapon.")
            print(f"Your attack power is now equal to {self.__atk}.")
        elif name in self.__inventory and self.__weapon_slot != {}:
            de_equip = self.__weapon_slot.popitem()
            self.pick_up_item(de_equip[0], 1)
            self.__atk -= de_equip[1]
            self.__weapon_slot[name] = power
            self.__atk += power
            print(f"You have now equipped {name} as a weapon.")
            print(f"Your attack power is now equal to {self.__atk}.")
        else:
            print("Could not find this item.")

    def equip_armor(self, name: str, power: int):
        if name in self.__inventory and self.__armor_slot == {}:
            self.__armor_slot[name] = power
            self.__hp += power
            print(f"You have now equipped {name} as an armor.")
            print(f"Your health is now equal to {self.__hp}.")
        elif name in self.__inventory and self.__armor_slot != {}:
            de_equip = self.__armor_slot.popitem()
            self.pick_up_item(de_equip[0], 1)
            self.__hp -= de_equip[1]
            self.__armor_slot[name] = name
            self.__hp += power
            print(f"You have now equipped {name} as an armor.")
            print(f"Your health is now equal to {self.__hp}.")
        else:
            print("Could not find that item")

    def move_player(self):
        where = input("=>")
        if where.lower() == "w":
            self.move_updown(-1)
        elif where.lower() == "s":
            self.move_updown(1)
        elif where.lower() == "d":
            self.move_leftright(1)
        elif where.lower() == "a":
            self.move_leftright(-1)
        else:
            return where


class EnemyModel(EntityModel):
    def __init__(self, posx: int, posy: int, map_model: str, name: str, ent_id: str, kind: str,
                 might: int, swift: int, life: int, spirit: int, mind: int):
        super().__init__(posx, posy, map_model, name, ent_id, kind)

        self.__might = might
        self.__swift = swift
        self.__life = life
        self.__spirit = spirit
        self.__mind = mind
        self.__atk = ceil(might * 1.25)
        self.__hp = floor(life * 10)
        self.__mana = floor(spirit * 5)
        self.__kind = "Enemy"

        self.__target = None

    def return_data(self):
        return (super().return_position(), super().return_map_model(), super().return_name(),
                super().return_id(), super().return_kind(), self.__might, self.__swift, self.__life,
                self.__spirit, self.__mind, self.__atk, self.__hp, self.__mana, self.__target)

    def return_atk(self) -> int:
        return self.__atk

    def return_target(self) -> object:
        return self.__target

    def return_kind(self) -> str:
        return "Enemy"

    def return_hp(self) -> int:
        return self.__hp

    def set_target(self, target: object):
        self.__target = target

    def search_and_destroy(self):
        if self.__target is not None:
            target_pos = self.__target.return_position()
            my_pos = self.return_position()

            if target_pos[0] > my_pos[0]:
                self.move_updown(1)
            elif target_pos[0] < my_pos[0]:
                self.move_updown(-1)
            elif target_pos[1] > my_pos[1]:
                self.move_leftright(1)
            elif target_pos[1] < my_pos[1]:
                self.move_leftright(-1)
            if my_pos == target_pos:
                self.__target.take_damage(self.return_name(), self.__atk)

    def take_damage(self, dmg: int):
        self.__hp -= dmg
        print(f"You have dealt {dmg} damage to {self.return_name()}.")