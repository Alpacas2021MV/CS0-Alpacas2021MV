from sys import *

def test():
    pass

def my_input(): 
    my_string = input()
    my_nums = []

    for i in range(len(my_string.split)):
        my_nums.append(int(my_string.split[i]))
        my_nums.sort(reverse = True)
        #Should now be [2, 2, 1, 1] (Greatest to Smallest)
    return my_nums, i

def my_output(my_nums, i):
    A = 0
    B = 0
    for A in my_nums:
        my_nums[i]
    for B in my_nums:
        my_nums[i+1]

    print(A)
    print(B)

def main():
    my_input()
    my_output()





if __name__ == "__main__":
    if (len(argv) == 2 and argv [1] == "test"):
        test()
    else:
        main()