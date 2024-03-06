class Animal: #declaring a class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def sit(self):
        print(f"{self.name} is sitting")

    def bark(self):
        print(f"{self.name} is barking")

dog = Animal("Puppy", 2) #creating a object
print(dog.name)
print(dog.age)
dog.sit()
dog.bark()