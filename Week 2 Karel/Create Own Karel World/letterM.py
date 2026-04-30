from karel.stanfordkarel import *

'''
Creatng letter M using Karel
'''
def main():
    

    #move karel one position forward
    move()
   
    #structure 
    vertical_upward_pillars()
    downward_diag_pillars()
    upward_diag_pillars()
    vertical_downward_pillars()
    
    
    

'''
building pillars vertically upwards 
'''
def vertical_upward_pillars():
  
    turn_left() #karel faces upwards
    
    while front_is_clear():

       
        put_beeper()
        move()
    # solving fence post problem
    
    put_beeper()
    turn_right()#karel faces east


#Diagonal pillars for letter M 
def downward_diag_pillars():
   
    #karel builds downwards diagonally 4 times
    #this is so to reach the centremost tip of the letter M
   
    for i in range(4):
        '''
        karel moves to next column, faces downwards 
        and moves one position downwards and places a pillar
        '''
        move()
        turn_right()
        move()
        put_beeper()
        turn_left()

'''
building upward diagonal pillars
'''
def upward_diag_pillars():
    '''
    karel moves to next column, faces upwards 
    and moves one position upward and places a pillar
        '''
    for i in range(4):
        move()
        turn_left()
        move()
        put_beeper()
        turn_right()
    
    
        

def  vertical_downward_pillars():
    turn_right()#karel faces downwards
    while front_is_clear():
        move()
        put_beeper()


def turn_right():
    for i in range(3):
        turn_left()

# don't change this code
if __name__ == '__main__':
    main()