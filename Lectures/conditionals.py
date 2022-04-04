"""
Name: Marcos Villarreal
Date: 02/25/22
"""
def main(): 
    money = int(input(f"How much money have you saved? "))
    ferrari = input(f"Do you have a ferrari [y/yes | n/no]: ")

    #if money > 1000000 or ferrari == "y/yes" then retire
    #Otherwise keep working 
    #          F                    F -> F            T
    if (money >= 1000000 and (ferrari == "y" or ferrari == "yes")): 
        print(f"Congrats, you can retire")
    else: 
        print(f"Back to work")


    #num = int(input("Please enter a whole number: "))
    #if (num %2 == 0 and num > 0):
    #    print(f"{num} is even and positive")
    #else: 
    #    print(f"{num} is odd")

main() 