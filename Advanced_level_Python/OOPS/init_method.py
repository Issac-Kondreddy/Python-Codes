class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

 #it is a special method used for initializing newly created objects
person1 = Person("Alice", 30)
person1.greet()  # Outputs: Hello, my name is Alice and I am 30 years old.
