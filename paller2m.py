from abc import ABC,abstractmethod
class car(ABC):
    def __init__(self,name,color,price):
        self.name=name
        self.color=color
        self.price=price
        self.speed=0
    @abstractmethod
    def stop(self):
        pass
class Bmw(car):
    def stop(self):
        self.stop=0
