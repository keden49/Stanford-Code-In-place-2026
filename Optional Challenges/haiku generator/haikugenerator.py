from ai import call_gpt

def main():
    # TODO: your code here
    #collecting user inputs 

    name = input("Enter your name: ")
    topic = input("Enter a topic: ")

    print ("Creating your haiku..." + "\n")

    ai_response = call_gpt(f"Create a haiku using name: {name} and topic: {topic}")
    

   
    print(ai_response)

if __name__ == "__main__":
    main()