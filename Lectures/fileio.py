import random
from sys import *
def tests():
    assert True == True
    print(f"All test cases passed!")


def main():
    #tests()
    input_lines = ""
    with open("..\\documents\\myfile.txt") as fin:
        input_lines = fin.read()

    my_string = input_lines.split()
    my_rand_choice = random.choice(my_string)
    print(f"{my_rand_choice}")


    #with open("documents\\myfile.txt", "w") as fout:
        #for line in my_string:
            # fout.write(f"{line}\n")
            #print(f"{line}", end='', file=fout)
        #data = fin.readlines()
        #for line in data:
        #    nums.append(int(line.strip()))
        #print(f"{nums}")
    #nums = []
    #fin = open("myfile.txt")
    #data = fin.readlines()
    #for line in data:
    #    #print(f"{line.strip}")
    #    nums.append(int(line.strip()))
    #print(f"{nums}")    
    #fin.close()

if __name__ == "__main__":
    print(f"{argv}")
    main()