class Father:
    def gardening(self):
        print("I enjoy gardening")

class Mother:
    def cooking(self):
        print("I love cooking")

# Inherits from both Father and Mother
class Child(Father, Mother):
    def hobbies(self):
        print("I enjoy sports")

# Creating an instance of Child
child = Child()
child.gardening()  # From Father
child.cooking()    # From Mother
child.hobbies()    # From Child itself
print(Child.__mro__)
