'''
Name: Marcos Villarreal 
Date: 02/28/22

This program will ask the user to input three sides of 
a triangle and will calculate the area and perimeter of the sides. 
Then, it should print on the screen the area and perimeter 

#Step 1: Prompt user to input three numbers (the three sides of the triangle hopefully)
#Step 2: Calculate the perimeter 
#Step 2a: Calculate the semi- perimeter
#Step 3: Calculate the area
#Step 4: print out area and perimeter 
#Step 5: Test to see if three sides actually make a triangle 
'''
#Step 1 
a = int(input("Please enter the length of the first side (a): "))
b = int(input("Please enter the length of the second side (b): "))
c = int(input("Please enter the length of the third side (c): "))

#Step 2
perimeter = a + b + c 

#Step 2a
'''
"s" is semi-perimeter
'''
s = perimeter // 2

#Step 3 
area = (s * (s - a) * (s - b) * (s - c))** 0.5

#Step 4 
print("The perimeter of this triangle with the lengths of", a, ",", b, "and", c, 
"would be: ", perimeter)

print("The area of this triangle with the lengths of", a, ",", b, "and", c, 
"would be: ", area)