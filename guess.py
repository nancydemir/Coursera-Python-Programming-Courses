# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
guess = ""
simple_number=0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global guess
    global secret_number
    guess=""
    secret_number=random.randint(0,100)
    print ("Secret number is: ",secret_number)
    # remove this when you add your code   
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game  
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
     pass
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    guess=int(guess)
    print ("Your guess was: ",guess)
    if guess == secret_number:
        print("YOU WIN!!YAY!YAY")
        print("STARTING A NEW GAME.....")
        new_game()
    elif guess > secret_number:
        print("Go Lower!")
    
# create frame
frame=simplegui.create_frame("Number Game",100,100)
frame.add_input("Input:",input_guess,50)

# register event handlers for control elements and start frame

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric
