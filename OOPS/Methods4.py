# Methods:- methods are functions that belong to objects.
class Student:
    college_name = "ABC College"

    def __init__(self, name, marks):
        self.name = name #obj attr > class attr
        self.marks = marks

    def welcome(self):
        print("Welcome Student", self.name)    

    def get_marks(self):
        return self.marks   

s1 = Student("Karan", 97)
s1.welcome() 
print(s1.get_marks())