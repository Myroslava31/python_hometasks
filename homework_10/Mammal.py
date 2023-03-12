from abc import ABC, abstractmethod
class Mammal(ABC):
    def __init__(self):
        self._hart = '4 chambers'
        self._hair = True
        self._smart = True
        self._feed_my_children = 'milk'
        self._rise_my_children = None
        self._food = None
        self.place = None
    @abstractmethod
    def carrying_about_children(self):...

    @abstractmethod
    def eat(self):...

    @abstractmethod
    def live(self):...
