# import Item
from src.item import Item


class MixinLan:
    """Mixin class initializing"""
    Language = "EN"

    def __init__(self):
        self.__language = self.Language

    @property
    def language(self):
        return self.__language

    def change_lang(self):
        """Change keyboard method initializing"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"

        return self.language


class Keyboard(Item, MixinLan):
    """Keyboard subclass initializing"""
    pass
