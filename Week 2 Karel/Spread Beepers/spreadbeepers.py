from karel.stanfordkarel import *

"""
Each row starts with a stack of beepers. Karel should pick them
up, one at a time, and spread them down the row. 
Caution! Karel can't count, and starts with infinite beepers in
her bag. How can you solve this puzzle?
"""


def main():
    move() #move karel to beepers location
    spread()
    """
    You should write your code to make Karel do its task in
    this function. Make sure to delete the 'pass' line before
    starting to write your own code. You should also delete this
    comment and replace it with a better, more descriptive one.
    """
#spread beepers

def spread():
    while beepers_present():
        pick_beeper()

        if beepers_present():#ensures after beepers end after starting position the code stops 
            move()
            find_empty_spot() #looks for position with empty slots 
            return_karel() #enables karel to pick beepers one at a time
            move() #ensures karel starts at beeper location

    #fence post problem 
    put_beeper()
    return_karel()

    
def find_empty_spot():
    while beepers_present():
        move()
    #if condition is false place beeper
    put_beeper()
        

            
            

def return_karel():
    turn_back() #karel faces west
    while front_is_clear():
        move()
    turn_back() #karel faces east
   

def turn_back():
     for i in range(2):
        turn_left()



# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()