
class KneadingMachine:
    # encapsualation
    def __init__(self, *args):
        self._switcher = False
        self._args = args

    def _add_ingridients_for_dough(self):
        ingridients = self._args
        return ingridients

    def _make_dough(self):
        self._add_ingridients_for_dough()
        self._switcher = True
        print('Making dough')
