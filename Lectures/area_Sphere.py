'''
Name: Marcos Villarreal
Date: 02/25/22

This program will find the area and circuminference a circle and display the answer

Step 1: Prompt user to enter the radius of a circle 
    Step 1a: Calculate the area 
Step 2: Calculate the circuminference) 
Step 3: Display the area and the circuminference
'''
#Step 1
import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi*radius*radius

#Step 2
C = 2*math.pi*radius
'''
This function finds the circuminference
'''
#Step 3
print("The area of this circle would be:", area,
"while the ciruminference will be", C)
