class Engine:
    def start(self):
        print("Engine starts")

    def stop(self):
        print("Engine stops")

class Car:
    def __init__(self):
        self.engine = Engine()  # Composition: Car "has-a" Engine

    def start(self):
        self.engine.start()  # Delegating the start method to the Engine class

    def stop(self):
        self.engine.stop()

my_car = Car()
my_car.start()  # Engine starts
my_car.stop()  # Engine stops
