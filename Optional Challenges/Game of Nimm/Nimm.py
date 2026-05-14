def main():
    tracker = 1 #keeps track of whose playing, starts at 1 
    stones = 20 #pile of stones
  
    '''
    game runs as long as there stones in the pile
    '''
    while stones != 0: 

        print(f"There are {stones} stones left.")
        move = int(input(f"Player {tracker} would you like to remove 1 or 2 stones? "))
        
        '''
        validating player's move if neither 1 or 2 the player 
        is prompted to remove the correct number stones 
        '''

        while move != 1 and move != 2:
            move = int(input("Please enter 1 or 2: "))
        
        print()
        # when one stone is left set the move to 1 
        if stones == 1:
            move = 1 

        stones = stones - move # subtract stones from pile 

        #preparing for next move
        if tracker == 1:
            tracker = tracker + 1 
        else:
            tracker = tracker - 1

    #when loop ends the next player wins

    print(f"Player {tracker} wins!")
        



if __name__ == '__main__':
    main()