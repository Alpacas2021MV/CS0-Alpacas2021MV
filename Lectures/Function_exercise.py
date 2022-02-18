'''
Name: Marcos Villarreal
Date: 02/18/22

Define a function that takes two numbers
and returns the product of the two numbers

Step 1: Define function to take two numbers
Step 2: Return product of two numbers from function
Step 3: Call function with some parameters
Step 4: Print out answer

'''


#Step 1
from operator import mul 

def multiply_nums(num1, num2):
    #Step 2
    return num1*num2

#Step 3
answer = multiply_nums(42, 5)

#Step 4
print("42 * 5 = ", answer)