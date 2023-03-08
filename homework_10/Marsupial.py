from homework_10.Mammal import Mammal

class Marsupial(Mammal):

    def __init__(self):
        super().__init__()
        self._rise_my_children = 'in a pouch'
        self._food = 'herbivores, omnivores and carnivores'
        self._place = 'Australasia, Wallacea and the Americas'

    def carrying_about_children(self):
        return f'We rise our children {self._rise_my_children} and feed them with {self._feed_my_children}'

    def eat(self):
        return f'We are {self._food}'

    def live(self):
        return f'We live in {self._place}'


