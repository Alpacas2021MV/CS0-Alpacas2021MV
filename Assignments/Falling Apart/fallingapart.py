from sys import *

def test():
    assert my_output([3, 2, 2]) == (5 ,2)
    assert my_output([7, 5, 2, 1]) == (9 ,6)
    assert my_output([9, 5, 3, 2, 1]) == (13 ,7)
    print("All testcases passed")

def my_input(): 
    tmp = input()
    my_string = input()
    my_nums = []
    my_string = my_string.split()
    for i in range(len(my_string)):
        my_nums.append(int(my_string[i]))
    my_nums.sort(reverse = True)
        #Should now be [2, 2, 1, 1] for example (Greatest to Smallest)
    return my_nums

def my_output(my_nums):
    alice = 0
    bob = 0
    alice_turn = True
    #https://github.com/KentGrigo/Kattis/blob/master/python/fallingapart.py Got the code below from here. 
    for nums in my_nums: 
        if alice_turn:
            alice += nums
        else:
            bob += nums
        alice_turn = not alice_turn
    return alice, bob

def main():
    test()
    my_nums = my_input()
    alice, bob = my_output(my_nums)
    print(alice, bob)

if __name__ == "__main__":
    if (len(argv) == 2 and argv [1] == "test"):
        test()
    else:
        main()