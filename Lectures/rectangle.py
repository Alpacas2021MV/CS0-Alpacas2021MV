'''
Name: Marcos Villarreal
Date: 02/09/22

This program will prompt for
two sides of a rectangle and will calculate 
the area and perimeter

Step 1: Prompt for side1 and side2 of a rectangle
Step 1a: Convert side1 and side2 to float
Step 2: Calculate area using side1 and side2
Step 3: Calculate perimeter using side1 and side2
Step 4: Print out area and perimeter
'''

#Step 1
side1= input("please enter one side of the rectangle: ")
side2= input("Please enter the other side of the rectangle: ")

#Step 1a
side1= float(side1)
side2= float(side2)

#Step 2
area= side1 * side2

#Step 3 
perimeter= (2 * side1) + (2 * side2)

#Step 4
print("The area of a rectangle with sides", 
    side1, side2,
     "is", area)