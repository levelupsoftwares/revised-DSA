# Design a function sum that take any number of arguments and return their total.The function should work
# for both fixed and variable number of arguments .Only Numerical Number will be provided
# Constraint & Edge Cases
#    * input all ways be number 
#    * No arguments should return 0
#    * Fucntion must handle  variable number of arguments 
#    * Negative Number should be handle correctly



def sum(*number):
    total = 0
    for n in number:
        total += n
    return total

        
print(sum(-5,5,5,1)) # 6
print(sum(7,5,1)) # 13
print(sum()) # 0