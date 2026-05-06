import random

def main():
    user_input = int(input("How many sides does your dice have? ")) #collect input from user $ convert to integer
    roll = random.randint(1,user_input) #generates a random integer between 1 and the number of sides on the dice
    print(f"Your roll is {roll}")

if __name__ == '__main__':
    main()