from abc import ABC, abstractmethod

class Device(ABC):
    @abstractmethod
    def connect(self):
        pass

class Mobile(Device):
    def connect(self):
        print("Mobile connected")
        
class Website(Device):
    def connect(self):
        print("Website connected")
