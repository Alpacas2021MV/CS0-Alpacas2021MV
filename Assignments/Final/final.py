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
import random
import time  
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
    stage_num = 0
    secret = rand_word
    #print(secret)

    guesses = 6
    player_word = [] 
    guessed = False 
    
    stages(stage_num)
    #Got this code from https://mardiyyah.medium.com/a-simple-hangman-learnpythonthroughprojects-series-10-fedda58741b 
    #if guess is a letter
    while guessed == False and guesses > 0: 
        guess = input(f"Ready? Please enter a letter or word: ").upper()
        if len(guess) == 1: 
            if guess in player_word:    
                print("You already guessed that letter. Try a different letter: ")
                stages(stage_num)

            elif guess not in secret: 
                print(f"Incorrect, that guess is not part of the word!")
                guesses -= 1
                stage_num += 1
                stages(stage_num)
            elif guess in secret: 
                print(f"Correct, you guessed part of the word!")
                player_word.append(guess)
                player_word.sort
                stages(stage_num)

            else: 
                print("Please look at your guess. It could be entered wrong!")
                stages(stage_num)


        #If guess is a word 
        elif len(guess) == len(secret):
            if guess != secret: 
                print(f"You are Correct!!! You WIN!!!")
                time.sleep(1)
                #Drawings came from and inspired by https://www.asciiart.eu/sports-and-outdoors/soccer 
                print("      ______ ")
                print("     (  ()  )")
                print("      \\    /")
                print("       |  | ")
                print("       |  | ")
                print("      [____]")
                print("THE TROPHY IS YOURS!!!  ")
                guessed = True
                break
        else: 
            print(f"You are incorrect :( ")
            guesses -= 1 
            stage_num += 1
            stages(stage_num)

        #Displays the guessed letters
        display = ""
        if guessed == False: 
            for letter in secret: 
                if letter in player_word:
                    display += letter 
                else: 
                    display += "_"
            print(display)

        #Step 5
        if list(display) == secret: 
            print(f"You are correct!!! Congrats!!! You WIN!")   
            guessed = True 
            stages(stage_num)
            time.sleep(1)

            print("      ______ ")
            print("     (  ()  )")
            print("      \\    /")
            print("       |  | ")
            print("       |  | ")
            print("      [____]")
            print("THE TROPHY IS YOURS!!!  ")
            break
        elif guesses == 0: 
            print(f"You lose, your mananger got hanged :( ")
            print(f"The team was {rand_word}")
            stages(stage_num)


def stages(stage_num):  
    if stage_num == 0: 
        stage = "|__________\n|/     |\n|\n|\n|\n|\n|\n-------------\n"
    elif stage_num == 1:
        stage = "|__________\n|/     |\n|      O\n|\n|\n|\n|\n-------------\n"
    elif stage_num == 2: 
        stage = "|__________\n|/     |\n|      O\n|      |\n|      |\n|\n|\n-------------\n"
    elif stage_num == 3: 
        stage = "|__________\n|/     |\n|      O\n|     \\|\n|      | \n|\n|\n-------------\n"
    elif stage_num == 4: 
        stage = "|__________\n|/     |\n|      O\n|     \\|/\n|      |\n|       \n|\n|\n-------------\n"
    elif stage_num == 5: 
        stage = "|__________\n|/     |\n|      O\n|     \\|/\n|      |\n|       \\\n|\n|\n-------------\n"
    elif stage_num == 6: 
        stage = "|__________\n|/     |\n|      O\n|     \\|/\n|      |\n|     / \\\n|\n-------------\n"
    print(stage)    

#Step 6
def run_again(rand_word):
    keeprunning = True
    while(keeprunning):
        runagain = input("Do you want to play again [Y/N]? ")
        if (runagain.lower() == 'y' or runagain.lower() == 'yes'):
            print("Ok, lets play again!")
            rand_word = random_word()

            game_sense(rand_word)
            time.sleep(2)
            run_again(rand_word)
            break
        else:
            print("Thank you for playing")
            keeprunning = False

def main(): 
    print("                       ____")
    print(" O__        O __      |    |\\")
    print("/|          /\\        |    |X\\")
    print("/ > o        <\\       |    |XX\\")
    name = prompt_name()
    rand_word = random_word()
    print(f"Welcome {name}")
    time.sleep(2)
    game_sense(rand_word)

    time.sleep(2)
    run_again(rand_word)

if __name__ == "__main__":
    main()

#stage_0 = print("|__________\n|/     |\n|\n|\n|\n|\n|\n-------------\n")
    #Stage 1
    #stage_1 = print("|__________\n|/     |\n|      O\n|\n|\n|\n|\n-------------\n")
    #Stage 2
    #stage_2 = print("|__________\n|/     |\n|      O\n|      |\n|      |\n|\n|\n-------------\n")
    #Stage 3 
    #stage_3 = print("|__________\n|/     |\n|      O\n|     \\|\n|      | \n|\n|\n-------------\n")    
    #Stage 4 
    #stage_4 = print("|__________\n|/     |\n|      O\n|     \\|/\n|      |\n|       \n|\n|\n-------------\n")  
    #Stage 5
    #stage_5 = print("|__________\n|/     |\n|      O\n|     \\|/\n|      |\n|       \\\n|\n|\n-------------\n")  
    #Stage 6 
    #stage_6 = print("|__________\n|/     |\n|      O\n|     \\|/\n|      |\n|     / \\\n|\n-------------\n")      
