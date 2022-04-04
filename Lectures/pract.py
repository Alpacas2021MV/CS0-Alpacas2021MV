'''
Name: Marcos Villarreal
Date: 03/14/22

This program is a different way of finding the area and perimeter of a triangle using functions and more things
It follows the same steps from the function homework assignment. View functions.py to see the steps
'''
from math import sqrt

def prompt_sides():
    print("Please enter 3 sides of a triangle: ")
    side1 = float(input("side 1: "))
    side2 = float(input("side 2: "))
    side3 = float(input("side 3: "))
    return side1, side2, side3

def calc_perim(side1, side2, side3):
    perimeter = side1 + side2 + side3
    return perimeter

def calc_area(side1, side2, side3, perimeter):
    #Step 8.1
    s = perimeter // 2
    area = sqrt(s*(s-side1)*(s-side2)*(s-side3))
    return area

def tests(): 
    assert calc_perim(2, 3, 4) == 9
    print("All test cases passed") 


def main():
    tests()
    #Step 7
    side1, side2, side3 = prompt_sides()

    #Step 12
    if (side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2):

        #Step 8
        perimeter = calc_perim(side1, side2, side3)

        #Step 9
        area = calc_area(side1, side2, side3, perimeter)

        #Step 10
        print(f"A triangle with sides, {side1}, {side2} and {side3} has an area of: {area} and a perimeter of: {perimeter}")
    else: 
        print(f"{side1}, {side2} and {side3} do not make a valid triangle. ")

main()