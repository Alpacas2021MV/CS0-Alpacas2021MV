'''
Name: Marcos Villarreal
Date: 05/17/22

This program will play out the game of Hangman

Step 1: Create a text file that has 20 English words
Step 2: Program chooses a random word from the list from step 1
Step 3: Ask player to guess the world one character at a time
Step 4: At the end, tell player whether they won or lost and ask if they want to play again
Step 5: 
'''
from re import L
import sys
import random
def tests(): 
    pass 

def prompt_name():
    print("Welcome to Hangman: Soccer edition")
    print("Words will be soccer clubs from (mostly) England and some in Germany and France")
    name = input("Please enter your name: ")
    print(f"Hello {name}, Please enter your guess (one letter at a time): ")
    return name

#Step 1
def random_word():
    input_lines = ''
    with open("..\\documents\\hm_words.txt") as fin:
        input_lines = fin.read()

    #Step 2
    my_string = input_lines.split()
    rand_word = random.choice(my_string)
    print(f"{rand_word}")
    return rand_word

def run_again():
    keeprunning = True
    while(keeprunning):
        runagain = input("Do you want to play again [Y/N]? ")
        if (runagain.lower() == 'y' or runagain.lower() == 'yes'):
            print("Ok, lets play again!")
            main()
            break
        else:
            print("Thank you for playing")
            keeprunning = False

def main(): 
    name = prompt_name()
    random_word()
    run_again()



if __name__ == "__main__":
    if (len(sys.argv) == 2 and sys.argv[1] == "test"):
        tests()
    else:
        main()
