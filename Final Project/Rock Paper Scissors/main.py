# This entrypoint file to be used in development. Start by reading README.md
from RPS_game import play, brahm, juliette, mehran, chris, human, random_player
from RPS import mudabbir


user = input("Enter your nickname \U0001F60E: ")
print()
competitor = input("Who do you want to play against? ").lower()

# validate user inputs 
while competitor not in ["chris", "mehran", "brahm", "juliette", "mudabbir", "random"]:

     competitor = input("Enter a choice among [chris, mehran, brahm, juliette, mudabbir, random]: ")
print()
num_games = input("How many Rounds Do you wish to play? ")

while not num_games.isdigit():
     num_games = input("Enter a valid number: ")

num_games = int(num_games)

hint = input("Hey do you want hints as you play the game [Y]es or [N]o? ")

while hint not in ["Y","N","Yes","No"]:
     hint = input("Enter a choice among [Y,N,Yes,No]: ")

# set up game against different opponents
if competitor == "brahm":
     
    play(human, brahm, num_games,competitor, user,verbose=True,hint = hint)
          
elif competitor == "chris":
     play(human, chris, num_games,competitor, user,verbose=True,hint = hint)

elif competitor == "mehran":
    play(human, mehran, num_games,competitor, user,verbose=True,hint = hint)

elif competitor == 'juliette':
     play(human, juliette, num_games,competitor, user,verbose=True,hint = hint)

elif competitor == 'mudabbir':
     play(human, mudabbir, num_games,competitor, user,verbose=True,hint = hint)

else:
     
     play(human, random_player, num_games,competitor, user,verbose=True)
    


      

     
           

    
       
    





