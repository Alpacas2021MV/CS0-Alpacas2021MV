'''
Name: Marcos Villarreal
Date: 03/28/22

This program will compute the values of sum, product, max, min, and average when given five numbers

Step 1: Define function that takes 5 numbers and calculates the sum 
Step 2: Define function that takes 5 numbers and calculates the product 
Step 3: Define function that calculates the average
Step 4: Define function that returns the largest value
Step 5: Define function that returns the smallest value
Step 6: Write test function and do test cases for all the previous functions
Step 7: Prompt user for five numbers
Step 8: Call functions and display the answers
'''
#Step 1 
def sum_nums(num1, num2, num3, num4, num5):
    sum = (num1 + num2 + num3 + num4 + num5) 
    return sum

#Step 2
def product(num1, num2, num3, num4, num5):
    multi = num1 * num2 * num3 * num4 * num5
    return multi

#Step 3
def average():
    #aver = sum // 5
    pass

#Step 4
def max():
    pass

#Step 5
def min():
    pass 

#Step 6
def tests():
    assert sum_nums(2 + 3 + 5 + 6 + 1) == 17
    assert sum_nums(1 + 2 + 3 + 4 + 5) == 15
    print("All test cases passed")

#Step 7
def prompt_nums(): 
    print("Please enter five numbers: ")
    num1 = float(input("Number 1: "))
    num2 = float(input("Number 2: "))
    num3 = float(input("Number 3: "))
    num4 = float(input("Number 4: "))
    num5 = float(input("Number 5: "))
    return num1, num2, num3, num4, num5

#Step 8
def main():
    tests()

    num1, num2, num3, num4, num5 = prompt_nums()
    print(f"The sum of {num1}, {num2}, {num3}, {num4} and {num5} is {sum_nums(num1, num2, num3, num4, num5)}")
main()