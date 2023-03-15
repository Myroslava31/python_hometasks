from abc import ABC, abstractmethod
#abstraction
class Oven(ABC):
    def __init__(self, temperature: int, time: int):
        #encapsualation
        self._temperature = temperature
        self._time = time

    @abstractmethod
    def _bake(self, temperature: int, time: int):...

