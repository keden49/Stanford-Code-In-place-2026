# Each year for a human is like 7.18 years for a dog
DOG_YEARS_MULTIPLIER = 7.18  

def main():
    
    human_years = input("Enter an age in calendar years: ")

    human_years = int(human_years) #converts string to integer

    dog_years = human_years * 7.18

    print(f"That's {dog_years} in dog years!")


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()