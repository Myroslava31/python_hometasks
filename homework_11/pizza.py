from homework_11.kneading_machine import KneadingMachine
from homework_11.oven import Oven

#Inheritance
class Pizza(Oven, KneadingMachine):
    # encapsualation
    def __init__(self, *args):
        super().__init__(temperature=350, time=5)
        # hiding
        self.__args = args
        self.__switcher = False


    def __add_ingridients_for_dough(self):
        ingridients = ('flour', 'eggs', 'yeast', 'water')
        return ingridients

        #Polymorphism
    def _make_dough(self):
        self.__add_ingridients_for_dough()
        self._switcher = True
        print('Making dough')

    def __prepare_filling(self, *args):
        print(f'Prepare next filling {args}')

    def _bake(self, temperature=350, time=5):
        print(f'Baking pizza with {temperature} for {time} minutes')

    # encapsualation
    def make_pizza(self, *args):
        self._make_dough()
        self.__switcher = False
        self.__prepare_filling(*args)
        self._bake()
