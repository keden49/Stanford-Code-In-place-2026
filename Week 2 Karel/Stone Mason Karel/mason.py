from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple
"""

def main():

    for i in range(2):
        build_column_upwards()
        move_next_column()
        build_column_downwards()
        move_next_column()

  
#moving upwards a column
def build_column_upwards():
    turn_left()#face upwards   
    put_beeper()#handles first beeper

    for i in range(4):
        move()
        put_beeper()
    turn_right() #end up in east facing position

def turn_right():
    for i in range(3):
        turn_left()  

def move_next_column():
    if front_is_clear(): #make sure its safe to move forward
        for i in range(4):
            move()
 
def build_column_downwards():
    turn_right() #face downwards 
    put_beeper()#handles first beeper 
    #place beepers downwards 
    for i in range(4):
        move()
        put_beeper()
    turn_left()# face correct position 



if __name__ == '__main__':
    main()