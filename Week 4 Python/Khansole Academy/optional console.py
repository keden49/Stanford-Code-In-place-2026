import random
def main():
    
    counter  = 0 #counter for correct addition problems 
    '''
    evaluates False for 3 since its equal to 3 and not less than it effectively stopping the loop 
    '''
    while counter < 3: 
        num1 = random.randint(10,99) #random 2 digit integer
        num2 = random.randint(10,99)

        target = num1 + num2 #correct answer

        print(f"Whats is {num1} + {num2}?")

        answer = int(input("Your answer: "))
        if target == answer:
            counter += 1 #incrementing counter

        print(f"Correct!\nYou've gotten {counter} correct in a row." if target == answer else f"Incorrect.\nThe expected answer is {target}")

    print("Congratulations! You mastered addition.") #when loop ends it means the counter has arrived at 3 
    



if __name__ == "__main__":
    main()