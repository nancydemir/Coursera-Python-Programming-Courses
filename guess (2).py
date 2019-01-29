
Run (Accesskey R)
  
Save (Accesskey S)
  
Download
  
Fresh URL
  
Open Local
  
Reset (Accesskey X)
 CodeSkulptor 
Docs
  
Demos
  
Viz Mode
 
1
# template for "Guess the number" mini-project
2
# input will come from buttons and an input field
3
# all output for the game will be printed in the console
4
​
5
import simplegui
6
guess = ""
7
​
8
# helper function to start and restart the game
9
def new_game():
10
    # initialize global variables used in your code here
11
    global guess
12
    guess=""
13
    # remove this when you add your code   
14
    
15
# define event handlers for control panel
16
def range100():
17
    # button that changes the range to [0,100) and starts a new game  
18
    # remove this when you add your code    
19
    pass
20
​
21
def range1000():
22
    # button that changes the range to [0,1000) and starts a new game     
23
     pass
24
    
25
def input_guess(guess):
26
    # main game logic goes here 
27
    int(guess)
28
    print ("Your guess was: ",guess)
29
    
30
​
31
    
32
# create frame
33
frame=simplegui.create_frame("Number Game",100,100)
34
frame.add_input("Input:",input_guess,50)
35
​
36
# register event handlers for control elements and start frame
37
​
38
# call new_game 
39
new_game()
40
​
41
# always remember to check your completed program against the grading rubric
42
​

('Your guess was: ', '5')
CodeSkulptor was built by Scott Rixner and is based upon CodeMirror and Skulpt.
