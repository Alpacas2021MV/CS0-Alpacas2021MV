'''
Name: Marcos Villarreal
Date: 02/21/22

This program will print various stages or parts of the hangman game
Step 1: Prompt user to enter their name. Make sure to store name as a function (# 7)
Step 2: Greet user and restate their name (#8). Then, state that the game is under construction
Step 3: Show stage 0, the beginning of Hangman
Step 4: Print stages 1 through 7
'''

#Step 1:
name= input("Please enter your name:")

#Step 2: 
print("Hello,", name)
import time 
print(time.sleep(2))
input("The hangman game is under construction, maybe you’ll get to play it in a few weeks...")
input("This is what various stages of the hangman game will look like…")
print(time.sleep(2))

#Step 3: 
print("This is Stage 0")
print("|__________") 						
print("|/    |") 
print("|") 	
print("|")
print("|") 	
print("|")
print("|") 				              
print("-------------") 

#Step 4: 