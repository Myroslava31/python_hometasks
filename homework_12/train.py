class Train:

    def __init__(self, train_number: int):
        self.__train_number = train_number
        self.__wagon = dict()

    def __len__(self):
        wagon_list = []
        for item in self.__wagon:
            if item == 0:
                continue
            else:
                wagon_list.append(item)
        print(wagon_list)
        return len(wagon_list)

    def __setitem__(self, key, value):
        self.__wagon[key] = value

    def __getitem__(self, item):
        return self.__wagon[item]

    def __str__(self):
        wagon_list = []
        for item in self.__wagon:
            if item == 0:
                wagon_list.append('[HEAD]')
            else:
                wagon_list.append(f'[{item}]')
        back = '-'.join(wagon_list)
        return f'<={back}'
