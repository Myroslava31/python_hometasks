from homework_10.Diprotodontia import Diprotodontia


class Vombatiformes(Diprotodontia):
    def __init__(self):
        super().__init__()
        self._food = 'herbivores'
        self._place = 'East Australasia and Tasmania'

    def eat(self):
        return f'We are {self._food}'

    def live(self):
        return f"We live in {self._place}"

    @staticmethod
    def find_relatives():
        return f'A lot of my family members are extinct'
