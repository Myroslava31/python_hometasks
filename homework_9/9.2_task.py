from datetime import date

class Employee:
    def __init__(self, name_surname: list, age: int, position: str, salary: int):
        self.__name_surname = name_surname
        self.__age = age
        self.__position = position
        self.__salary = salary

    @classmethod
    def creation_with_date(cls, name_surname: list, date_of_birth: date, position: str, salary: int):
        """If you have date of birth instead of age this function calculates the age"""
        today = date.today()
        age = today.year - date_of_birth.year - ((today.month, today.day) < (date_of_birth.month, date_of_birth.day))
        return cls(name_surname, age, position, salary)

    @property
    def name_surname(self):
        return self.__name_surname

    @name_surname.setter
    def name_surname(self, new_name_surname: list):
        if isinstance(new_name_surname, list):
            self.__name_surname = new_name_surname

    @name_surname.deleter
    def name_surname(self):
        del self.__name_surname

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age: int):
        if 18 < new_age < 120:
            self.__age = new_age
        else:
            raise TypeError("We can't hire non adult")

    @age.deleter
    def age(self):
        del self.__age

    @property
    def position(self):
        return self.__position

    @property
    def salary(self):
        return self.__salary

    @position.setter
    def position(self, new_position: str):
        positions = ['developer', 'QA', 'manager', 'analyst', 'accountant', 'sales', 'administrator']
        for position in positions:
            if position == new_position:
                self.__position = new_position
        if self.__position != new_position:
            raise TypeError("Only positions of developer, QA, manager, analyst, accountant, sales, administrator are supported")

    @salary.setter
    def salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
        else:
            raise TypeError('Only integer which is lager than previous salary is supported')

    def salary_increase(self) -> int:
        return int(self.__salary + (self.__salary * 0.1))

    def trainings(self):
        if self.__position == 'manager':
            return 'Send employee on the training'
        else:
            return "Let employee work"

    @staticmethod
    def hire_new_employee(hard_skills: int, soft_skills: int):
        """This function takes two int from 0 to 100"""
        if 0 < hard_skills < 100 and 0 < soft_skills < 100:
            if hard_skills + soft_skills > 120:
                return 'You can hire this person'
            else:
                return "This person doesn't correspond to the requirements"
        else:
            return 'Please enter two integer numbers from 1 to 100'

