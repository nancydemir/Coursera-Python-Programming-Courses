# Echo an input field
###################################################
# Student should add code where relevant to the following.
import simplegui 
message=""
# Handlers for input field    
# Create frame and assign callbacks to event handlers
def get_input(text):
    print text
    
frame = simplegui.create_frame("Input Echoer", 200, 200)
inp=frame.add_input("Enter Text",get_input,50)
#print "hello",inp.get_text()
# Start the frame animation
frame.start()
###################################################
# Test

get_input("First test input")
get_input("Second test input")
get_input("Third test input")

###################################################
# Expected output from test

#First test input
#Second test input
#Third test input
