import random

def main():
    print("Khansole Academy")
    
    '''
    this program generates random addition problems for users
    '''

    num1 = random.randint(10,99) #first random number
    num2 = random.randint(10,99) #second random number
   
    target = num1 + num2 #answer

    print(f"What is {num1} + {num2}?")
    answer = int(input("Your answer: "))
    print("Correct!" if target == answer else f"Incorrect.\nThe expected answer is {target}")
    
    
if __name__ == '__main__':
    main()