from sys import *

def test():
    pass

def my_input(): 
    my_string = input()
    my_nums = []

    for i in range(len(my_string.split)):
        my_nums.append(int(my_string.split[i]))
        my_nums.sort(reverse = True)
        


def main():
    pass




if __name__ == "__main__":
    if (len(argv) == 2 and argv [1] == "test"):
        test()
    else:
        main()