class Wagon:
    def __init__(self, wagon_number: int):
        self.__wagon_number = wagon_number
        self.__passengers = ['Petrenko', 'Kuzmenko', 'Ivanenenko', 'Ivanchuk', 'Sydorenko', 'Jonsoniuk']

    def __setattr__(self, key, value):
        if isinstance(value, str):
            self.__passengers.append(value)
        super().__setattr__(key, value)


    def __len__(self):
        return len(self.__passengers)

    def __str__(self):
        return f'[{self.__wagon_number}]'

if __name__ == '__main__':
    wagon1 = Wagon(1)
    print(wagon1)
    setattr(wagon1, 'passengers', 'Dmytruk')
    print(len(wagon1))
