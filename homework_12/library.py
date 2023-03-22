class Library:

    def __init__(self, author: str, name: str, year: int,):
        self._author = author
        self._name = name
        self._year = year

    def __str__(self):
        return f'{self.__class__.__name__}: \n{self.__dict__}'
