import random
import time

NUM_PAIRS = 3


truth_list = []

# Milestone 1 
# create pairs 

for i in range(NUM_PAIRS):

    truth_list.append(i)
    truth_list.append(i)


# Milestone 2 
# shuffle 

random.shuffle(truth_list)

 # Milestone 3 
 # Create displayed list

displayed_list = ["*" for _ in range(len(truth_list))]


# Milestone 6 
# Simulate Turns

def main():

    # Game should end when the displayed list and truth list match 

    while displayed_list != truth_list:
       
       
        print(displayed_list)

        # get valid indexes 
        index1,index2 = Validate_index()

        # Milestone 5 
        # Check Match 

        if truth_list[index1] != truth_list[index2]:

            print(f"Value at index {index1} is {truth_list[index1]}")
            print(f"Value at index {index2} is {truth_list[index2]}")
            print("No match. Try again.")
            input("Press Enter to continue...")
            time.sleep(1.5)
            clear_terminal()
        
        else:
        
            # Update displayed list
            displayed_list[index1] = truth_list[index1]
            displayed_list[index2] = truth_list[index2]
            print("Match!")
            time.sleep(1.5) # delay python from clearing terminal
            clear_terminal()
        
    
    # User has won game
    print(displayed_list)
    print("Congratulations! You won!")


def Validate_index():

    # Validation for first index

    while True:

        num1 = input("Enter an index: ")
        
        # repeatedly prompt user if index is non valid
        # add condition for 0 since 0 is a Falsy value 
        if not get_valid_index(num1):

            continue # restarts the loop
        else:
            index1 = int(get_valid_index(num1))

            
            break # exit loop completely

        
    # Validation for second index   
    while True:
        
        num2 = input("Enter an index: ")

        if num1 == num2:
            print("You entered the same index twice. Try again.")
            continue
        

        if not get_valid_index(num2):

            continue # restarts the loop
        else:
            index2 = int(get_valid_index(num2))
            break
    
    return index1,index2

# Milestone 4 
 # Get valid indices
   
   

def get_valid_index(index):

    # check if number 

    if index.isdigit():
        index = int(index)

    else:
        print("Not a number. Try again.")
        return False

    # check if index is in bound 

    if index >= 0 and index < len(truth_list):
        
        
        if displayed_list[index] == '*':
            
            # returns string value to avoid returning false

            return str(index)
        else:

            print("This number has already been matched. Try again.")
            return False 

    else:
        print("Invalid index. Try again.")
        return False

 
def clear_terminal():
    for i in range(20):
      print('\n')

if __name__ == '__main__':
    main()