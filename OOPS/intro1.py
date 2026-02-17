#  To map with real world scenarios, we started using objects in code.
# This is called Object Oriented Programming.

#   Class :- class is a blueprint for creating objects.
#         class  Student:
#          name = "Karan Kumar"

#   Object :- instance of class.
#    s1 = Student()
#      print(s1.name)


# Example..

class Student: #class
    name = "Karan"
    roll = 47

s1 = Student() # Object
print(s1.name)

s2 = Student()
print(s2.name)
print(s2.roll)

