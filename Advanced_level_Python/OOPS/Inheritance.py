class Dog:
    def __init__(self,name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is sitting")

    def bark(self):
        print(f"{self.name} is barking")

class ShihTzu(Dog):

    def __init__(self,name,age, color):
        super().__init__(name, age)
        self.color = color

    def show_color(self):
        print(f"{self.name} is of {self.color}")


snoppy = ShihTzu("snoppy", 20, "red")
snoppy.show_color()
snoppy.sit()
snoppy.bark()