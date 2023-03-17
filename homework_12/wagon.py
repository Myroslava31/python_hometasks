class Wagon:
    def __init__(self, wagon_number: int):
        self.__wagon_number = wagon_number
        self.__passengers = ['Petrenko', 'Kuzmenko', 'Ivanenenko', 'Ivanchuk', 'Sydorenko', 'Jonsoniuk']

    def __setattr__(self, key, value):
        if isinstance(value, str):
            self.__passengers.append(value)

    def __len__(self):
        return len(self.__passengers)

    def __str__(self):
        return self.__wagon_number


