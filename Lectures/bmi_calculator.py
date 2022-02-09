'''
Name: Marcos Villarreal
Date: 02/09/22

This program will calculate the BMI of a person
BMI = kg/m^2

Step 1: Prompt user to enter weight and height
Step 1a:Convert values to floats
Step 2: Calculate BMI using imputed values 
Step 3: Print out BMI
'''
#Step 1
weight= input("Please enter your weight in kg: ")
height= input("Please enter your height in meters: ")

#Step 1a
weight= float(weight)
height= float(height)

#Step 2
bmi= weight/height**2

#Step 3 
print("Your BMI with weight", weight, "and height", height, "is", bmi)