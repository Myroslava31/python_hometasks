from homework_10.Vombatiformes import Vombatiformes


class Koala(Vombatiformes):
    def __init__(self):
        super().__init__()
        self.__food = 'eucalypt leaves'
        self.__place = 'forests of East Australasia'
        self.__hobby = 'sleep'
        self.__abilities = 'swim'

    def eat(self):
        return f'I eat {self.__food}'

    def live(self):
        return f"I live in {self.__place}"

    @staticmethod
    def get_my_hobby():
        return f'I am very active'

    def __get_my_abilities(self):
        return f'I can {self.__abilities}'
