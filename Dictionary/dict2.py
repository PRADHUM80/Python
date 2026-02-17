# nested Dictionary ...
# Example..

student = {
    "name" : "Pradhum Kumar",
    "subject" : {   # Nested Dect...
        "phy" : 97,
        "chem" : 98,
        "math" : 95
    }
}

print(student)
# Subject Print
print(student["subject"])
# proper subject 
print(student["subject"]["chem"])