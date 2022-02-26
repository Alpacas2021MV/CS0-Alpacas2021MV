'''
Name: Marcos Villarreal 
Date: 02/28/22

This program will ask the user to input three sides of 
a triangle and will calculate the area and perimeter of the sides. 
Then, it should print on the screen the area and perimeter 

#Step 1: Prompt user to input three numbers (the three sides of the triangle hopefully)
#Step 2: Test to see if lengths given actually make a triangle  
#Step 3: Calculate the perimeter
#Step 3a: Calculate the semi perimeter
#Step 4: Calculate the area 
#Step 5: print out area and perimeter
'''

#Step 1 
a = int(input("Please enter the length of the first side (a): "))
b = int(input("Please enter the length of the second side (b): "))
c = int(input("Please enter the length of the third side (c): "))

#Step 2 
#Got confused on this part, I found this code from here (Hopefully this counts as a citation)
# https://tutorialspoint.dev/algorithm/geometric-algorithms/check-whether-triangle-valid-not-sides-given

def check_Validity(a, b, c): 
    '''
    This functions checks to see if the inputed lengths actually form a triangle
    '''
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return False
    else: 
        return True    

if check_Validity(a, b, c): 
    print("Triangle is Valid")
else: 
    print("Triangle is Invalid")

#Step 3
perimeter = a + b + c 

#Step 3a
#"s" is the semi-perimeter
s = perimeter // 2

#Step 4 
area = (s * (s - a) * (s - b) * (s - c))** 0.5

#Step 5 
print("The perimeter of this triangle with the lengths of", a, ",", b, "and", c, 
"would be: ", perimeter)

print("The area of this triangle with the lengths of", a, ",", b, "and", c, 
"would be: ", area) 
