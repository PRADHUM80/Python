# Conditional Statements..
# Syntax:- if-elif-else

# Traffic Light Code..
light  = input("light : ")
if(light == "red"):
    print("stop")
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")



# Grades of Students...
marks = int(input("Marks : "))
if(marks >= 90):
    print("O - Grade")
elif(marks >= 80):
    print("A - Grade")
elif(marks >= 60):
    print("B - Grade")
elif(marks >= 40):
    print("D - Grade")
else:
    print("F - Grade")
