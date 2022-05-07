'''
Name: Marcos Villarreal
Date: 05/17/22

This program will play out the game of Hangman

Step 1: Create a text file that has 20 English words
Step 2: Program chooses a random word from the list from step 1
Step 3: Prompt user for their name
Step 4: Ask player to guess the world one character at a time
Step 5: At the end, tell player whether they won or lost 
Step 6: Ask player if they want to play again
'''
import sys
import random

def tests(): 
    pass 
#Step 1
def random_word():
    input_lines = ''
    with open("documents\\hm_words.txt") as fin:
        input_lines = fin.read()

    #Step 2
    my_string = input_lines.split()
    rand_word = random.choice(my_string)
    "Here is where the word is put in a list and is separated" 
    rand_word = list(rand_word.lower())
    return rand_word

#Step 3
def prompt_name():
    print("Welcome to Hangman: Soccer edition")
    print("Words will be soccer clubs/teams from (mostly) England and some in Germany and France")
    name = input("Please enter your name: ")
    return name

#Step 4
def game_sense(rand_word):
    target_word = rand_word
    #Beginning of the Game 
    print("|__________") 						
    print("|/    |") 
    print("|") 	
    print("|")
    print("|") 	
    print("|")
    print("|") 				              
    print("-------------") 
    print(f"Your Guess (One letter at a time): ")
    print(target_word)
     
#Step 6
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
    rand_word = random_word()
    game_sense(rand_word)
    run_again()

if __name__ == "__main__":
    if (len(sys.argv) == 2 and sys.argv[1] == "test"):
        tests()
    else:
        main()
