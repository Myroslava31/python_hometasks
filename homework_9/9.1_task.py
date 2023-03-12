class NovaPoshta:

    def __init__(self, number: int, address: dict, type: str):
        """Type can be 'office' or 'point'"""
        self.__number = number
        self.__address = address
        self.__type = type
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, new_number: int):
        if isinstance(new_number, int) and 0 < new_number < 100000:
            self.__number = new_number
        else:
            raise TypeError('Only integer in range 0-100000 is supported')

    @number.deleter
    def number(self):
        del self.__number

    @property
    def address(self):
        return f'{self.__address.get("city")}, {self.__address.get("street")}, {self.__address.get("building")}. {self.__address.get("where")}. {self.__address.get("privacy")}'

    @address.setter
    def address(self, new_address: dict):
        if isinstance(new_address, dict):
            self.__address = new_address
        else:
            raise TypeError('Only dict is supported')

    @address.deleter
    def address(self):
        del self.__address

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, new_type: str):
        if new_type == 'office' or new_type == 'point':
            self.__type = new_type
        else:
            raise TypeError("Only 'office' and 'point' values are supported")
    @type.deleter
    def type(self):
        del self.__type

    @staticmethod
    def calculate_price(weight: float, price = 5) -> float:
        """Calculates price of parcel. Price for kilo is fixed number and equals 5 gryvnas"""
        price = 40 + (weight * price)
        return price

