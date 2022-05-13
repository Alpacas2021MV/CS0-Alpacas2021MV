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
from dis import dis
import random
import time 

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
    rand_word = list(rand_word.upper())
    return rand_word

#Step 3
def prompt_name():
    print("Welcome to Hangman: Soccer edition")
    print("Words will be soccer clubs/teams from (mostly) England and some in Germany and France")
    name = input("Please enter your name: ")
    return name

#Step 4
def game_sense(rand_word):
    secret = rand_word
    print(secret)

    len(secret)
    guesses = 6
    player_word = [] 
    guessed = False 
    print()

    #Got this code from https://mardiyyah.medium.com/a-simple-hangman-learnpythonthroughprojects-series-10-fedda58741b 
    while guessed == False and guesses > 0: 
        guess = input(f"Ready? Please enter a letter or word: ").upper()
        if len(guess) == 1: 
            if guess in player_word:    
                print("You already guessed that letter. Try a different letter: ")
            elif guess not in secret: 
                print(f"Incorrect, that guess is not part of the word!")
                guesses -= 1
                print(player_word)
            elif guess in secret: 
                print(f"Correct, you guessed part of the word!")
                player_word.append(guess)
                player_word.sort
                print(player_word)
            else: 
                print("Please look at your guess. It could be entered wrong!")

        elif len(guess) == len(secret):
            if guess == secret: 
                print(f"You are Correct!!! You guessed the word")
                guessed = True
                break 
            else: 
                print(f"You are incorrect :( ")
                guesses -= 1 
            
        stat = ""
        if guessed == False: 
            for letter in secret: 
                if letter in player_word:
                    stat += letter 
                else: 
                    stat += "_"
            print(stat)

        if stat == secret: 
            print(f"You are correct!!! You guessed the word")   
            guessed = True 
            break
        elif guesses == 0: 
            print(f"You lose, you man got hanged :( ")
    #for i in range(len(secret)):
    #    if guess.upper() == secret: 


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
    print(f"Welcome {name}")
    time.sleep(2)

    game_sense(rand_word)
    run_again()

if __name__ == "__main__":
    main()
