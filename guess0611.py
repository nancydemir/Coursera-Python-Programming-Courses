# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random
import math
guess = ""
secret_number=0
max_guesses=7
range=100

# helper function to start and restart the game:
def new_game():
    # initialize global variables used in your code here
    global guess
    global secret_number
    global guess_tries
    guess_tries=0
    guess=""
    print ("\nSTARTING NEW GAME.......GUESS A NUMBER") 
    inp.set_text("")
    if range==1000:
        print("IN RANGE 1 to 1000\n")
        print("You have a total of 10 guesses.\n")
        secret_number=random.randrange(0,1000)
        #print ("Secret number is: %d"%secret_number)
        guesses_left=10
        #return
    else:
        print("IN RANGE 1 to 100\n")
        print("You have a total of 7 guesses.")
        secret_number=random.randrange(0,100)
        #print ("Secret number is: %d"%secret_number)
        guesses_left=7
        #return
    
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number 
    global max_guesses
    max_guesses=7
    global range
    range=100    
    new_game() 

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    global max_guesses
    max_guesses=10
    global range
    range=1000    
    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global secret_number
    global max_guesses
    global guess_tries   
    guess=int(guess)  
    
    print ("Your guess was: %d\n"%guess)
    guess_tries=guess_tries+1 
    guesses_left=max_guesses-guess_tries
    print ("Guesses left: %d"%guesses_left) 
    if guess==secret_number:         
        print("THAT IS CORRECT!!! YOU WIN!!!\n") 
        inp.set_text("")
        new_game()
    elif guesses_left==0:
        print ("Sorry,...you have exceed your allowable guesses.\n")
        print ("The secret number was %d\n"%secret_number)
        new_game()
    
    elif guess > secret_number:
        print("Go Lower!\n")
        inp.set_text("")        
        return
    else:
        print("Go Higher!\n")
        inp.set_text("")
        return           
          
# create frame
frame=simplegui.create_frame("Guess a Number Game",200,200,300)
label = frame.add_label("CLICK A BUTTON TO CHOOSE RANGE")
inp=frame.add_input("Input:",input_guess,50)

# register event handlers for control elements and start frame
def button_handler():
    pass
frame.add_button("Guess in Range of 1 to 100", range100)
frame.add_button("Guess in Range of 1 to 1000", range1000)
frame.start()

# call new_game 
new_game()

# always remember to check your completed program against the grading rubric

