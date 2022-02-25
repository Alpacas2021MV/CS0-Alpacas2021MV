'''
Name: Marcos Villarreal 
Date: 02/28/22

This program will ask the user to input three sides of 
a triangle and will calculate the area and perimeter of the sides. 
Then, it should print on the screen the area and perimeter 

#Step 1: Prompt user to input three numbers (the three sides of the triangle hopefully)
#Step 2: Calculate the area 
#Step 3: Calculate the perimeter 
#Step 4: print out area and perimeter 
#Step 5: Test to see if three sides actually make a triangle 
'''
#Step 1 
side1 = input("Please enter the first side: ")
side2 = input("Please enter the second side: ")
side3 = input("Please enter the last side: ")

#Step 2
def calc_triangle_area(side1, side2, side3):
    '''
    This function takes in the three sides inputed 
    and will calculate the area using Heron's formula
    '''
    s = (side1 + side2 + side3)//2
    return s

#Step 3 
def calc_triangle_perim(side1, side2, side3): 
    '''
    This function takes in the three sides inputed before 
    and will calculate the perimeter
    '''
    pass

#Step 4
def main(): 

    pass