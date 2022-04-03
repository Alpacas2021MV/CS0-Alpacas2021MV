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
import random
#Step 1
def prompt_name():
    print("Welcome to -- Guess the Number -- The Game! ")
    name = input("Please enter your name: ")
    print(f"Hello {name}, I'm thinking of a number between 1 and 20.")
    return name

#Step 2
def random_number():
    print(f"You got six attempts to guess the number.")
    ran_number = random.randint(1, 20)
    print(f"the random number is {ran_number}")
    return ran_number

#Step 3
def more_guesses(ran_number, name):
    count_wins = 0
    count_losses = 0
    for i in range(6):
        guess = int(input("Take a guess: "))
        #Step 3a
        if guess == ran_number:
            print(f"Congratulations {name}! You won")
            print(f"You guessed the number in {i+1} attempt(s)")
            count_wins + 1
            break
        #Step 4
        else:
            print(f"You are not correct")
            if guess < ran_number:
                print(f"Guess is too low. Guess again")
            else: 
                print(f"Guess is too high. Guess again")
    #Step 3b            
    if guess != ran_number:
        #Step 5
        print(f"Game over :( , You lose. The number was {ran_number}.")
        count_losses + 1
    return guess, count_wins, count_losses 

#Step 6
def run_again(ran_number, name, count_wins, count_losses): 
    keeprunning = True
    while(keeprunning):
        runagain = input("Do you want to play again [Y/N]?")
        if (runagain.lower() == 'y' or runagain.lower() == "yes"):
            print("Ok, lets play again!")
            random_number()
            more_guesses(ran_number, name)
            run_again(ran_number, name, count_wins, count_losses)
            break
        else:
            print("Thank you for playing!")
            stats(count_wins, count_losses)
            keeprunning = False

def stats(count_wins, count_losses): 
    print(f"Wins: {count_wins}")
    print(f"Losses: {count_losses}")

def main():
    name = prompt_name()
    ran_number = random_number()
    count_wins, count_losses = more_guesses(ran_number, name)
    run_again(ran_number, name, count_wins, count_losses)

main()