print("Guess Kevin's age you have 3 attempts!\n")
#import emoji

target = 20
hint = "it is two digits and ends with a zero"
print(f"Hint: {hint}")

#counter = 3 #keeps track of user inputs

'''use emoji unicodes to make the interface more interactive'''
for i in range(3):
    
    print(f'You have {i+3} attempts left \U0001F440' +"\n" if i == 0 else f'You have {i+1} attempts left \U0001F605'+"\n" if i == 1 else f'You have {i-1} attempt left \U0001F976'+"\n") #different print statements for different entries 

    
    guess = int(input("Enter your guess: ")) #collect user input 
    
    if guess == target:
        print("You got it right!")
        break # exist loop
        
    elif guess > 20:
        print("Too high!")
        print("Try again\n")

    else:
        print("Too low!")
        print("Try again\n")

if guess != target:
    print("Time's up!")



