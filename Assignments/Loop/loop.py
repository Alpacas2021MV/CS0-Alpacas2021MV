'''
Name: Marcos Villarreal 
Date: 04/04/22

This program will play out a game called "Guess the Number." The program will think of a number, 1 to 20, and the player will have 
six attempts to guess that number. 

Step 1: Prompt user for their name and greet the player. Also include a welcome messenge 
Step 2: Prompt user to guess a number between 1 and 20. Program should choose a random number every time. 
Step 3: Continue prompting player to make guesses until they win or lose (six attempts allowed)
Step 3a: If they win with six or less guesses, tell player they won 
Step 3b: If the player doesn't guess the number correctly, tell player they lost. 
Step 4: For every wrong guess, inform player whether guess is too high or too low
Step 5: At the end of the game, reveal what the secret number was. 
Step 6: Ask if player wants to play again
Step 7: Once player quits, display their stats with how many games were played with number of wins and losses. 
'''
#Step 1
def prompt_name():
    print("Welcome to -- Guess the Number -- The Game! ")
    name = input("Please enter your name: ")
    return name

def main():
    name = prompt_name()
    #Step 2
    print(f"Hello {name}, I'm thinking of a number between 1 and 20.")
    print(f"You got six attempts to guess the number.Take a guess: ")

main()