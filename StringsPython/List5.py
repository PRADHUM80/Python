# Lists and Tupples.

# lists :- a built in data type that stores set of values
# it can store elements of different types (int, string, float etc)
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
print(marks[0])

student = ["karan", 95.4, 17, "Delhi"]
print(student)


# List Slicing :-

# Similar to String Slicing.
mark = [87, 64, 33, 95, 76]
print(mark[1:4])
print(mark[-3:-1])


# List Methods
# 1 appned
list = [2, 1,3]
list.append(4)
print(list)

# 2 Sort :- ascending order
list.sort()
print(list)

# 3 sort (reverse = True) Descending order
list.sort(reverse = True)
print(list)

# 4 insert element
list.insert(4, 5)
print(list)

# 5 remove
list.remove(5)
print(list)

# 6 pop
list.pop(1)
print(list)


# List. show many .....