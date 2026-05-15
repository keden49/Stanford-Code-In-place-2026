import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Game!")
    print('--------------------------------')
    
    score = 0
    for i in range(NUM_ROUNDS):
        comp_no = random.randint(1,100)
        user_no = random.randint(1,100)
        
        print(f"Round {i+1}")
        print(f"Your number is {user_no}")
        guess = input("Do you think your number is higher or lower than the computer's?: ").lower()

        #validating users logic 

        while guess != 'lower' and guess!= 'higher':

            guess = input("Please enter either higher or lower: ")

        target = "lower" if comp_no > user_no else "higher"

        print(f"You were right! The computer's number was {comp_no}" if target == guess else f"Aww, that's incorrect. The computer's number was {comp_no}" )
        if target == guess:
            score += 1 #score is only added if user is correct
        print(f"Your score is now {score}")
        print()

    print("Thanks for playing!")

    
if __name__ == "__main__":
    main()