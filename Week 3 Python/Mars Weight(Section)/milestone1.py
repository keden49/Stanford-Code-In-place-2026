"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""
mars_constant = 0.378
def main():

    #collect user input 
    
    earth_weight = float(input("Enter a weight on Earth: "))
    mars_weight = earth_weight * mars_constant 
    mars_weight = round(mars_weight, 2) #rounding off to 2 decimal places 

    print(f"The equivalent weight on Mars: {mars_weight}")
if __name__ == "__main__":
    main()