class Teacher:
    def __init__(self, name):
        self.name = name

class School:
    def __init__(self, name, teachers):
        self.name = name
        self.teachers = teachers  # Aggregation: School "has-a" Teachers

teacher1 = Teacher("Mrs. Smith")
teacher2 = Teacher("Mr. Jones")

school = School("Sunnydale High", [teacher1, teacher2])

for teacher in school.teachers:
    print(teacher.name)
