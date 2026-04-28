from karel.stanfordkarel import *

def main():
    # at the beggining of each loop karel is at same position in a row 
    # that row has to be clear 

    '''
    at the end of a loop they are two scenarios 
    Scenerio 1 
    karel has moved up 1 row up and to starting position
    
    Scenerio 2

    Karel has hit a dead end
    '''


    while left_is_clear():
        clearpath() #clear beepers
        return_to_start()#return to start
        turn_right() #turn to face upward
        move()
        turn_right() #karel has to face east

#fencepost problem/accounting for the last beeeper 
    clearpath()

 
def clearpath():
    '''
    move to wall while picking beepers
    '''

    while front_is_clear(): 
        if beepers_present():
            pick_beeper()
        move() #moves regardless of beeper or not

#fencepost problem/accounting for the last beeeper 

    if beepers_present():
      pick_beeper()
  
# Karel has to turn around and move to starting position    
        
def return_to_start():
    turn_around()    
    while front_is_clear():
        move()

#function to turn back
def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()

if __name__ == '__main__':
    main()