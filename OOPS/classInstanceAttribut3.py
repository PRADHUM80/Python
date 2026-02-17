#  Class.attr
# obj.attr


class Student:
    college_name = "ABC College"
    name = "anonymous" # class attr


    def __init__(self, name, marks):
        self.name = name #obj attr > class attr
        self.marks = marks
        print("Adding new Student")

s1 = Student("Karan", 97)
print(s1.name)        