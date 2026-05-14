from karel.stanfordkarel import *

# Here is a place to program your Section problem

def main():
    build_columns()
    
def build_columns():
    while front_is_clear():
        move()
        if beepers_present():
            turn_left() #karel moves upwards
            build_upwards()
            turn_right() #karel faces east
            move()
            build_downwards()


def build_upwards():
    for i in range(2):
        move()
        put_beeper()
    
def turn_right():
    for i in range(3):
        turn_left()

def build_downwards():
    turn_right() #karel faces downwards
    put_beeper() #fence post problem
    for i in range(2):
        move()
        put_beeper()
    turn_left() #karel faces east
if __name__ == '__main__':
    main()