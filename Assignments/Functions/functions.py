'''
Name: Marcos Villarreal 
Date: 03/14/22

This program will perform some arithmetic operations when given two numbers using functions

Step 1: Define function that adds the numbers and return sum
Step 2: Define function that multiplies the two numbers and return product
Step 3: Define function that divides first number by second number and return quotient
Step 4: Define function that takes two numbers, subtracts second from first and return difference
Step 5: Define function that find reminder of first number divided by second number
Step 6: Define function that find the first to the power of the second number and returns the value
Step 7: Define a function that takes a number and returns the square-root of the number. 
Step 8: Prompt user to enter two numbers
Step 9: Call all functions and display answers with descriptions 
Step 10: Write a test function that to automatically test each function
Bonus step: Write function that finds the larger of the two numbers
'''
import time
#Step 1
def add(num1, num2): 
    add_ans = num1 + num2
    return add_ans

#Step 2 
def multi(num1, num2):
    mul_nums = num1 * num2
    return mul_nums

#Step 3
def divide(num1, num2):
    div_nums = num1 // num2
    return div_nums

#Step 4
def subtract(num1, num2):
    sub_num = num2 - num1 
    return sub_num

#Step 5 
def remind(num1, num2):
    rem = num1%num2
    return rem

#Step 6 
def power(num1, num2):
    pow_num = num1 ** num2
    return pow_num

#Step 7 
def sqrt(num1):
    sq = num1 ** 0.5
    return sq

#Step 8 
def main():
    num1 = int(input("Please enter the first number: "))
    num2 = int(input("Please enter the second number: "))

#Step 8
    print(f"The sum of {num1} and {num2} is {add(num1, num2)}")
    time.sleep(1)
    print(f"The product of {num1} and {num2} is {multi(num1, num2)}")
    time.sleep(1)
    print(f"The quotient of {num1} and {num2} is {divide(num1, num2)}")
    time.sleep(1)
    print(f"The difference of {num1} and {num2} is {subtract(num1, num2)}")
    time.sleep(1)
    print(f"The reminder between {num1} and {num2} is {remind(num1, num2)}")
    time.sleep(1)
    print(f"The value of {num1} to the power of {num2} is {power(num1, num2)}")
    time.sleep(1)
    print(f"The square root of {num1} is {sqrt(num1)}")

main()