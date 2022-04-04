'''
Name: Marcos Villarreal
Date: 03/28/2022

This program will print a multiplication table. The limit is 31 x 31. 
'''
def print_table(table_size):
    print(f"{'':>4}", end='')
    for i in range(table_size):
        print(f"{i+1:>4}", end='')
    print("")

    for i in range(table_size+1):
        print(f"----", end='')
    print(" ")

    for i in range(table_size):
        print(f'{i+1:<4}', end= '')
        for j in range(table_size):
            print(f"{(j+1)*(i+1):>4}", end='')
        print(" ")

def input_table_size():
    promptagain = True
    while(promptagain):
        size_of_table= input("Please enter the size of the multiplication table to print:")
        if(size_of_table.isdecimal()):
            promptagain = False
        else:
            print("Please enter a whole number")
        return int(size_of_table)

def main():
    size_of_table = input_table_size()
    print_table(size_of_table)

main()