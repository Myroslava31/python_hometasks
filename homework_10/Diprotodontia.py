from homework_10.Marsupial import Marsupial

class Diprotodontia(Marsupial):
    def __init__(self):
        super().__init__()
        self._food = 'herbivores and omnivores'
        self._place = 'Australasia and Wallacea'

    def eat(self):
        return f'We are {self._food}'

    def live(self):
        return f"We live in {self._place} and don't live in water"
