class CustomIterator:
    def __init__(self, sequence, start_index: int, end_index: int):
        if start_index < 0 or end_index < 0:
            raise ValueError("Start and end index can't be negative")
        if end_index > len(sequence):
            raise ValueError("End index can't be bigger than the length of the sequence")
        if start_index >= end_index:
            raise ValueError("Start index can't be bigger or equal to the end index")
        self.__sequence = sequence
        self.__start_index = start_index
        self.__end_index = end_index

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start_index < self.__end_index:
            value = self.__sequence[self.__start_index]
            self.__start_index += 1
            return value
        else:
            raise StopIteration

