from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def materialcounter(self):
        pass


class Palto(Clothes):
    def __init__(self, sise, name):
        super().__init__(name)
        self.sise = sise

    @property
    def materialcounter(self):
        material = (self.sise / 6.5 + 0.5)
        return material


class Suit(Clothes):
    def __init__(self, height, name):
        super().__init__(name)
        self.height = height

    @property
    def materialcounter(self):
        material = (self.height * 2 + 0.3)
        return material


versache_palto = Palto(46, 'Palto versache')

print(versache_palto.name)
print(versache_palto.materialcounter)

versache_suit = Palto(40, 'Suit versache')

print(versache_suit.name)
print(versache_suit.materialcounter)
