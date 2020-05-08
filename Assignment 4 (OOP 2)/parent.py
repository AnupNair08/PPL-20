import abc
#Base class
class Animal(metaclass=abc.ABCMeta):
    def __init__(self):
        self.kingdom = 'Animalia'
    def speak(self):
        print('Animals can speak')
    def virtual(self):
        print(self.kingdom)
    @abc.abstractmethod
    def abstract(self):
        pass