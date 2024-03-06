class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return "Woof!"


class ShihTzu(Dog):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return "Yap!"
def dog_talk(dog):
    print(dog.speak())

generic_dog = Dog('Rex', 2)
shihtzu_dog = ShihTzu('Buddy', 5, 'white')

dog_talk(generic_dog)  # Outputs: Woof!
dog_talk(shihtzu_dog)  # Outputs: Yap!
