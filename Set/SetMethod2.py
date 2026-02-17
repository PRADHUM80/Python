# Set Methods..

# 1 .add
collection = set() #empty set; syntax
collection.add(1)
collection.add(2)
collection.add(3)
collection.add(4)
collection.add("apnaCollege")
collection.add((1, 2, 3)) # tupples..
collection.add(2) # not exists duplicate value..
print(collection)

# 2 .remove
collection.remove(2)


# 3 .clear()
print(len(collection))  # 5

collection.clear()
print(len(collection))  # 0


# 4.pop()

collect = {"hello", "apnacollege", "world"}
print(collect.pop())
print(collect.pop())
# random value genereated.

# 5 .union( ) :- combine both set values & returns a new value..
set1 = {1, 2, 3}
set2 = {2, 3, 4}
print(set1.union(set2))
print(set1)
print(set2)


# 6 .intersection() :- combines common values & returns new
print(set1.intersection(set2))


