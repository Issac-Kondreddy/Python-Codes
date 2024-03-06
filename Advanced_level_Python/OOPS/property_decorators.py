class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        "The 'name' property."
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty.")
        self._name = value

    @name.deleter
    def name(self):
        del self._name
