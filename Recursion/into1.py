# Recursion :-  when a function calls itself repeatedly.
# loop vs Recursion vise versa...



# def show(n):
#     if(n == 0): # base case
#         return
#     print(n)
#     show(n-1)

# show(5)


# factorial 

# def fact(n):
#     if(n == 1 or n == 0):
#         return 1
#     return fact(n-1) * n

# print(fact(5))


# ques
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)    