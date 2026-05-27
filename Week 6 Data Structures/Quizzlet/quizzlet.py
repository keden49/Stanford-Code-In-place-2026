def main():
    translations = {
        "hello": "hola",
        "dog": "perro",
        "cat": "gato",
        "well": "bien",
        "us": "nos",
        "nothing": "nada",
        "house": "casa",
        "time": "tiempo"
    }

    keys = list(translations.keys()) # list of questions 
    targets = list(translations.values()) # list of desired responses
    score = 0 

    


    # the loop runs 8 times
    for i in range(8):

        # collect user inputs 
    
        answer = input(f"What is the Spanish translation for {keys[i]}? ")
        
        if targets[i] == answer:
            print("That is correct!")
            score += 1 # increase score

        else:
            print(f"That is incorrect, the Spanish translation for {keys[i]} is {targets[i]}.")

    print(f"You got {score}/8 words correct, come study again soon!")



if __name__ == '__main__':
    main()