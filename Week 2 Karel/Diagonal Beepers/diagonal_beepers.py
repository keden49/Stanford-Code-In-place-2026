from karel.stanfordkarel import *


def main():
   
   #runs endlessly until karel encounters a wall

    while front_is_clear():
         
        put_beeper() #place beeper 

        #move up diagonally
        turn_left() 
        move()
        turn_right()
        move()

    #place beeper in final position
    put_beeper()
    
def turn_right():
    # defines turn_right as 3x turn_left
    for i in range(3):
        turn_left()


if __name__ == '__main__':
    main()