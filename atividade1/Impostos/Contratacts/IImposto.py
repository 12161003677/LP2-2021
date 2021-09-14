from abc import ABC, abstractmethod

class IImposto(ABC):

    @abstractmethod
    def calcular(self):
        pass