# Basic operation...

# Concatenation..
str1 = "apna"
str2 = "college"
final_str = str1 + " " + str2  #Empty space count hota hai
print(final_str)



# Length .. . letter count
print(len(str1))
print(len(str2))
print(len(final_str))



# indexing... position
str = "Apna_College"
print(str[0])
print(str[5])




# Slicing..
# Accessing parts of a string
# str[ starting_idx : ending_idx]  ending_idx is not included

st = "ApnaCollege"  # 012345678910
print(st[1:4]) #pna
print(st[4:12]) #college

# Negative index :-  
st1 = "apple"
print(st1[-5:-1])
print(st1[-4:-1])

