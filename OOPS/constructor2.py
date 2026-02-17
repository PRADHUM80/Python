# init_Function.

# Constructor :- all classes have a funvtion called _init_(), which is always executed when the object is being initiated.
# The Self Parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.



# class Student: #class
#     # name = "Karan"
#     # roll = 47
#     def __init__(self, fullname):
#         self.name = fullname
#         print("Adding new Student database")
  

# # s1 = Student() # Object
# # print(s1.name)
# # print(s1.roll)

# s1 = Student("Pradhum") # fullname.
# print(s1.name) 

# Repeat..
class Student:
    # default constructors
    # def __init__(self):
    #     pass
    # Parameterized Constructor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("adding new student in Database..")

s1 = Student("Karan", 97)
print(s1.name, s1.marks)

s2 = Student("Arjun", 88)
print(s2.name, s2.marks)

