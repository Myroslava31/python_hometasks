from abc import ABC, abstractmethod
class Mammal(ABC)
    def __init__(self, hart: str, hair: bool, smart: bool, feed_my_children: str, rise_my_children, food: str, place: str):
        self._hart = '4 chambers'
        self._hair = True
        self._smart = True
        self._feed_my_children = 'milk'
        self._rise_my_children = None
        self._food = None
        self.place = None
    @abstractmethod
    def carrying_about_children(self, feed_my_children, rise_my_children):...

    @abstractmethod
    def eat(self, food):...

    @abstractmethod
    def live(self, place):...
