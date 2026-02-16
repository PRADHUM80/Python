# Single Line TernaryOperator.....
# <var> = <val1> if <condition> else <val2>

food = input("food : ")
eat = "yes" if food == "cake" else "no"
print(eat)

#2 <st1> if <condition> else <st2>
food = input("food : ")
print("sweet") if food == " cake" or food == "jalebi" else print("no")

# 3. Clever if ...
# <var> = (false_val, true_val) [<condition>]
age = int(input("age : "))
vote = ("yes" , "no") [age >= 18]
