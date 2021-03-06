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
def multiply_nums(*args):
    """
    This function takes in two numbers as parameters 
    and returns those numbers multiplied together. 
    """
    #Step 2
    #print(f"{args}")
    mul_nums = args[0] * args[1]
    return mul_nums

   # return mul_nums

def tests():
    assert multiply_nums(3, 4) == 42
    assert multiply_nums(7, 8) == 56
    assert multiply_nums(7, 1) == 7
    print(f"All test cases passed")

def main():
    tests()

def main(): 
    number1 = int(input("Please enter a number: "))
    number2 = int(input("Please enter another number: "))
    #Step 3
    answer = multiply_nums(number1, number2, 123, 82, 5)
    #Step 4
    #print(f"{number1} * {number2} = {answer}")

main() 