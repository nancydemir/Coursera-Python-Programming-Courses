# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math
guess = ""
secret_number=random.randint(0,100)
guess_tries=0

# helper function to start and restart the game:
def new_game():
    # initialize global variables used in your code here
    global guess
    global guess_tries
    guess_tries=0
    global secret_number
    #secret_number=random.randint(0,100)
    guess=""
    print ("STARTING NEW GAME....GUESS A NUMBER:")
    
# define event handlers for control panel
def range100():
    global secret_number 
    # button that changes the range to [0,100) and starts a new game  
    secret_number=random.randint(0,100)
    new_game()
    print ("Secret number is: %d"%secret_number)
   

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    secret_number=random.randint(0,1000)
    new_game()
    print ("Secret number is: %d\n"%secret_number)
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global guess_tries
    guess=int(guess)
    print ("Your guess was: %d\n"%guess)
    guess_tries+=1
    print ("guess tries is: %d"%guess_tries)
    if guess_tries>7:
        print ("Sorry, you lose")
        new_game()
        return
    while guess!=secret_number:
        if guess > secret_number:
             print("Go Lower!\n")
             inp.set_text("")
             return
        elif guess < secret_number:
             print ("Go Higher!\n")
             inp.set_text("")
             return           
    else:
        print("THAT IS CORRECT!!! YOU WIN!!!\n") 
                
# create frame
frame=simplegui.create_frame("Guess a Number Game",200,200,300)
label = frame.add_label("CLICK A BUTTON TO CHOOSE RANGE")
inp=frame.add_input("Input:",input_guess,50)

# register event handlers for control elements and start frame
def button_handler():
    pass
range100 = frame.add_button("Guess in Range of 1 to 100", range100)
range1000 = frame.add_button("Guess in Range of 1 to 1000", range1000)
frame.start()

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric

