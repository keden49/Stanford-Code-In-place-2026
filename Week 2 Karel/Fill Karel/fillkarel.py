from karel.stanfordkarel import *

"""
Karel should fill the whole world with beepers.
"""


def main():

    '''
    this loop runs as long  as karel ends up 
    in the same starting position at each new row
    '''

    while left_is_clear(): #upward part must be unoccupied 
        fill_row()
        return_to_start()
        move_up()
    #fencepost problem
    fill_row()
  
def fill_row():
    put_beeper() #fence post problem
    while front_is_clear():
        move()
        put_beeper()

#karel moves to starting position

def return_to_start():
    turn_around()
    while front_is_clear():
        move()
   
#karel moves up
def move_up():
    turn_right()
    move()
    turn_right()
    

def turn_around():
    for i in range(2):
        turn_left()

def turn_right():
    turn_around()
    turn_left()



if __name__ == '__main__':
    main()