# Methods...


# 1 myDict.keys() :- returns all keys

student = {
    "name" : "Pradhum Kumar",
    "subject" : {   # Nested Dect...
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student.keys())
# total no of keys
print(len(list(student.keys())))

# 2 value() ;- return values

print(student.values())
# typecast
print(list(student.values()))

# 3 .items() :- return all (key , val) pairs as tuples

print(student.items())
# typecast
print(list(student.items()))
# or
pairs = list(student.items())
print(pairs[0]) #pairs of index.


# 4 .get("Key") :- returns the key according to value
print(student["name"])  # dont use this methods.
# or
print(student.get("name")) # use this methods..


# 5 .update(newDict) :-- insert the specified items to the dictionary
student.update({"city" : "Ara"})
print(student)