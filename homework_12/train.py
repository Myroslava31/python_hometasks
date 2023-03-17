class Train:

    def __init__(self, train_number: int):
        self.__train_number = train_number
        self.__vagon = dict()

    def __len__(self):
        return len(self.__vagon)

    def __setitem__(self, key, value):
        self.__vagon[key] = value

    def __getitem__(self, item):
        return self.__vagon[item]
