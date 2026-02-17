# MEthods that don't use the self parameter (work at class level).
class Student:
    college_name = "ABC College"

    def __init__(self, name, marks):
        self.name = name #obj attr > class attr
        self.marks = marks
    @staticmethod
    def hello():
        print("Hello")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
            print("hi",self.name, "your avg score is : ", sum/3)    

s1 = Student("Karan", [99,98,97])
s1.get_avg()
s1.hello()