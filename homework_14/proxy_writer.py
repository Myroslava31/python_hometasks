from homework_14.reader import Reader
from homework_14.writer import Writer
from txt_reader import TxtReader
from txt_writer import TxtWriter

class Proxy(Reader, Writer):
    def __init__(self, txt_reader: TxtReader, txt_writer: TxtWriter):
        self.__result = ''
        self.__is_actual = False
        self.__reader = txt_reader
        self.__writer = txt_writer

    def read(self):
        if self.__is_actual:
            return self.__result
        else:
            self.__result = self.__reader.read()
            self.__is_actual = True
            return self.__result

    def write(self, new_data: str):
        if new_data != self.__result:
            self.__writer.write(new_data)
            self.__is_actual = False

