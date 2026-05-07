from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should be able to find
the midpoint
"""

def main():
    
    '''
    ill attempt to make karel create diagonals from root ends
    and placing beepers at each step and once its at the centre it moves downwards to the centre position
    '''
    find_point_of_intersection() 
    set_world_midpoint() #set midpoint
    clear_world()
    move_to_centre()


# turning functions 

def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    for i in range(3):
        turn_left()   



'''
karel sets path diagonally but upwards
'''

def upward_diagonals():
   
    while left_is_clear():
       
       turn_left()
       move()
       turn_right()
       move()
       put_beeper()
       
'''
moves karel downwards
to set up next path diagonally
'''

def move_downwards():
    turn_right() #karel faces down
    while front_is_clear():
        move()
    turn_right() #karel faces west

'''
karel sets path diagonally but downwards
'''

def downward_diagonals():
   
    move() #first move
    while no_beepers_present():
        turn_right()#karel faces upwards
        move()
        if no_beepers_present():
            put_beeper()
            turn_left()#karel faces west
            #only moves if it is safe 
            if front_is_clear():
                move()
        
        else:
            turn_left() #ensures karel faces west for even world

    '''
    their is two case scenerios where karel might end up depending on which world karel occupies
    odd world karel faces upwards and ends up at centre 
    even world karel faces west ends up at leftmost centre
    '''
    
    
    

'''
sets midpoint
'''

def set_world_midpoint():
    turn_left() #karel faces downwards
    while front_is_clear():
        move()
    put_beeper()
    


 
#bring it all together 

def find_point_of_intersection():
     upward_diagonals()
     move_downwards()
     downward_diagonals()
#returns karel to starting position
def return_karel():
    turn_right() #karel faces west
    while front_is_clear():
        move()
    turn_around()



def clear_world():
    return_karel()
    #karel should move to next row to avoid removing midpoint
    move_up()

    while left_is_clear():
        clear_row()
    #fencepost problem
    clear_row()


def clear_row():
    while front_is_clear():
        if no_beepers_present():
            move()
        else:
            pick_beeper()
            move()
    #fencepost problem
    if beepers_present():
        pick_beeper()

    #returns to staring position
    turn_around()
    while front_is_clear():
        move()
    turn_around()
    move_up()

'''
moves karel up each row while clearing
'''
def move_up():
    turn_left()
    if front_is_clear():
        move()
    turn_right()  
'''
karel returns to midpoint
'''
def move_to_centre():
    turn_right() #karel faces downwards
    while front_is_clear(): #karel moves to first row 
        move()
    turn_left()
    while no_beepers_present():
        move()
        

if __name__ == '__main__':
    main()