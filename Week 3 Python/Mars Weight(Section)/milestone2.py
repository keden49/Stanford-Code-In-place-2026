"""
Prompts the user for a weight on Earth
and prints the equivalent weight on Mars.
"""
mars_constant = 0.378
Mercury = 37.6 / 100
Venus = 88.9 / 100
Mars = 37.8 / 100
Jupiter = 236.0 / 100
Saturn = 108.1 / 100
Uranus = 81.5 / 100
Neptune = 114.0 / 100

# convert planets to dictionaries for easier implementations 

planet_list = ['Mercury','Venus','Mars','Jupiter','Saturn','Uranus','Neptune']
planet_list = [word.lower() for word in planet_list] #converts all words to lowercase 

planet_variables = [Mercury, Venus, Mars, Jupiter, Saturn, Uranus, Neptune]

planets_dictionary = {key:value for key,value in zip(planet_list,planet_variables)}


def main():

    #collect user input 
    
    while True:
        user_inputs= input("Enter a weight on Earth and a planet(separate them using a comma): ")
        if ',' not in user_inputs:
            print("please separate your inputs with a comma")
            continue
        break

    
    earth_weight, planet = user_inputs.split(",")
    earth_weight = float(earth_weight)
   
    
    #convert user input to lowercase
    #this allows the fn to be flexible to user inputs 
    #strip removes any leading whitespaces 
    planet = planet.lower().strip()
    #check whether user input is valid 
    if planet not in planets_dictionary:

        print(f"{planet} is not a valid planet")
        return #end function
    planets_weight =earth_weight * planets_dictionary[planet] # fetching value directly from created dictionary
    planets_weight = round(planets_weight, 2) #rounding off to 2 decimal places 

    print(f"The equivalent weight on {planet}: {planets_weight}")
if __name__ == "__main__":
    main()

