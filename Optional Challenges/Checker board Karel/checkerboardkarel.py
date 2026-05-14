from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


'''
this code follows two unique patterns
thats the pattern this code tries to mimic
'''


def main():
    while left_is_clear():
        first_pattern()
        second_pattern()

    '''
    move karel to previous row to determine state of checkboard
    if its odd it should move back and perfom the first pattern and return to start position
    else it should return to the start position since the row it was on is already filled by second pattern
    '''
    state_of_checkboard()

    #for even checkboards
    if beepers_present():
        complete_task()
    
    else:
        turn_back() #karel faces upwards
        move()
        turn_right()#karel faces east
        first_pattern() #for odd checkboard
        turn_right() #karel faces downwards
        complete_task()


    


    
def state_of_checkboard():
    turn_right()
    move()

   
  

def first_pattern():
    put_beeper()
    while front_is_clear():
        move()
        if front_is_clear(): #avoids karel running into a wall after first move 
            move()
            put_beeper()
    return_karel()

'''
second is the first pattern just shifted by one 
'''

def second_pattern():
    #for worlds more than 2 columns 
    if front_is_clear():
        move()
        first_pattern()
    
    else:
        #if the world is only one column move karel to the next row above
        turn_left()
        move()
        turn_right()#karel faces east
    
      
        
    


   
   
#returns karel to starting position       
def return_karel():
    turn_back()
    while front_is_clear():
        move()
    move_up()
    turn_right() #karel faces east 
    
def turn_right():
    for i in range(3):
        turn_left()
    

def turn_back():
    for i in range(2):
        turn_left()
#moves karel one position forward        
def move_up():
    turn_right()
    if front_is_clear():
        move()

#returns karel back to where it started 
def complete_task():
    while front_is_clear():
        move()
    turn_left() #karel faces east
    

# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()