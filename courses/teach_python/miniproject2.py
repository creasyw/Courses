# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
from random import randint
import simplegui as sg

# initialize global variables used in your code
result = 0
limit = 0
ingame = 0

# define event handlers for control panel
    
def range100():
    # button that changes range to range [0,100) and restarts
    return randint(0, 99)
    
def range1000():
    # button that changes range to range [0,1000) and restarts
    return randint(0, 999)

def get_input(guess):
    # main game logic goes here	
    n = int(guess)
    global limit
    if limit == 0:
        print "Sorry, the allowance is used up!"
        if ingame == 1:
            button1()
        else:
            button2()
    else:
        limit -= 1        
        if n == result:
            print "Correct!"
        elif n > result:
            print "The number of remaining guesses is ", limit
            print "Your guess is ", n, ", but it is Higher."
        else:
            print "The number of remaining guesses is ", limit
            print "Your guess is ", n, ", but it is Lower." 

def button1():
    global result, limit, ingame
    ingame = 1
    limit = 7
    result = range100()
    print "Now guessing from 0 to 99."
    
def button2():
    global result, limit, ingame
    ingame = 2
    limit = 10
    result = range1000()
    print "Now guessing from 0 to 999." 
    
# create frame
frame = sg.create_frame("Home", 100, 200)

# register event handlers for control elements
frame.add_button("Range: 0-100", button1)
frame.add_button("Range: 0-1000", button2)
frame.add_input("Input your guess:", get_input, 100)

# start frame
frame.start()
button1()

# always remember to check your completed program against the grading rubric
