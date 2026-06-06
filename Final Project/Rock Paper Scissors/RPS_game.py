

import random
import os
import time
def play(player1, player2, num_games, competitor,user,verbose=False,hint = "N"):
    p1_prev_play = ""
    p2_prev_play = ""
    results = {user: 0, competitor: 0, "tie": 0}
    print("\n"+ "Let the Games begin!" + "\n")
    

    for _ in range(num_games):
        print(f"Current Score {results}" + "\n")
        print("💡 Counters: R ➔ S | P ➔ R | S ➔ P (➔  =  Beats)" + "\n")
        p1_play = player1(p2_prev_play,competitor = competitor,hint = hint)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results["tie"] += 1
            winner = "Tie."
        elif (p1_play == "P" and p2_play == "R") or (
                p1_play == "R" and p2_play == "S") or (p1_play == "S"
                                                       and p2_play == "P"):
            results[user] += 1
            winner = f"{user} wins."
        elif p2_play == "P" and p1_play == "R" or p2_play == "R" and p1_play == "S" or p2_play == "S" and p1_play == "P":
            results[competitor] += 1
            winner = f"{competitor} wins."

        if verbose:
            print("Calculation scores...")
            # set sleep time to avoid rushing the game
            time.sleep(1)
            print(f"{user}: {p1_play} | {competitor}: {p2_play}")
            print(winner)
            time.sleep(1.5) # sleep again for opponent to view results
            clear_terminal()

        

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results[user] + results[competitor]

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results[user] / games_won * 100

    print("Final results:", results)
    print(f"{user} win rate: {win_rate}%")
    print()
    print("You are the champion \U0001F3C6" if results[user] > results[competitor] else f"{competitor} won this time" + "\n" + "Don't give up try again! \U0001F60A")


    return (win_rate)


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def brahm(prev_play, counter=[0]):

    counter[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    return choices[counter[0] % len(choices)]


def mehran(prev_opponent_play, opponent_history=[]):

    if not prev_opponent_play:
        prev_opponent_play = "R"
    opponent_history.append(prev_opponent_play)

   
    
    last_ten = opponent_history[-10:]
    
    most_frequent = max(last_ten, key=last_ten.count)

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[most_frequent]


def chris(prev_opponent_play):
    if prev_opponent_play == '':

        prev_opponent_play = "R"
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prev_opponent_play]

# smartest player 
# tracks player based on the last two plays

def juliette(prev_opponent_play,
          opponent_history=[],
          play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):
    
    
    if not prev_opponent_play:
        prev_opponent_play = 'R'
    

    opponent_history.append(prev_opponent_play)

    last_two = "".join(opponent_history[-2:])

    if len(last_two) == 2:
        play_order[0][last_two] += 1
    
    
    potential_plays = [
        prev_opponent_play + "R",
        prev_opponent_play + "P",
        prev_opponent_play + "S",
    ]

    sub_order = {
        k: play_order[0][k] # pulls value out 
        for k in potential_plays if k in play_order[0]
    }
    
    '''
    predicts your next play based on frequencies of pairs you like to take
    '''
    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]


'''
human player interface 
'''



# juliette move tracker 
combinations = {"RR": 0,"RP": 0,"RS": 0,"PR": 0,"PP": 0,"PS": 0,"SR": 0,"SP": 0,"SS": 0}

sequence_tracker  = {}
n = 3

def human(prev_opponent_play,competitor,opponent_history = [],history = ["R"],hint = "N"):

    global combinations,sequence_tracker,n
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    play = ""
    if not prev_opponent_play:
        pass
    else:
        opponent_history.append(prev_opponent_play)
        
        # helping out
        if competitor == "brahm":
            print(f"{competitor} recent plays: {opponent_history}")

            if hint in ("Y","Yes") and len(opponent_history) >= 5:
                 
                 print("Shhh ...\U0001F92B This is a secret hint")
                 print("Check Brahm's 5 past previous moves to identify repeating sequences")
                 print("To win you must counter each 5 repeating sequence")
            print()
        
        if competitor == "chris":
            last_move = history[-1]
            ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
            
            if hint == "Y" or hint == "Yes":
                print(f"Hint: Chris assumes you will just repeat your last play ('{last_move}').")
                print(f"He's planning to play '{ideal_response[last_move]}' to beat it.")
                print("What will you play to counter him?")
            else:
                print(f"Tracker: Chris only counters your last move ('{last_move}').")
                print(f"To win you must counter his own counter move to {last_move}")
            print()
                 
         

        if competitor == "mehran":

            most_frequent = max(history[-10:],key = history[-10:].count) 
            
            if hint == "Y" or hint == "Yes":
                print(f"Shhh ...\U0001F92B This is a secret hint")
                print(f"Mehran expects you to play {most_frequent} next")
                print(f"To win you must counter his own counter move which is {ideal_response[most_frequent]}")
                
            else:
                 print(f"Your most frequent move is currently {most_frequent}")
                 print(f"To win you must counter Mehran's counter move to {most_frequent}")
            print()
            
        if competitor == "juliette":

             # last two plays 

            prev2= ''.join(history[-2:])
            # Keep the same tracker as Abby 

            if len(prev2) == 2:

                combinations[prev2] += 1

            # get last play which will be previous move for abbey

            last_play = history[-1] # prevents crashing

            # potential plays 

            expected_plays = [last_play + play for play in ['R','P','S']]

            #  counts of expected plays 

            expected_counts = {k:combinations[k] for k in expected_plays if k in combinations}

            # get the Juliettes prediction

            expected_prediction = max(expected_counts, key = expected_counts.get)
            last_move = expected_prediction[-1]
            print(f"Your most frequent pair of moves is {expected_prediction}")
            
            if hint == "Y" or hint == "Yes":
                print(f"Hint: Juliette predicts you will play '{last_move}'.")
                print(f"She's planning to play '{ideal_response[last_move]}' to beat it.")
                print("What will you play to counter her?")
            else:
                print(f"Tracker: Juliette noticed your frequent pair '{expected_prediction}'.")
                print("She's preparing her next move based on the end of that sequence. Choose wisely.")
            print()    
            
        
        if competitor == "mudabbir":
                

                if len(history) > n:

                    seq ="".join(history[-n:])
                    last_seq = "".join(history[-(n + 1):])
                    if last_seq not in sequence_tracker:
                            sequence_tracker[last_seq] = 1
                    else:
                            sequence_tracker[last_seq] += 1
                    possible_seq = [seq + move for move in ["R","P","S"]]
                    freq = {}
                    for possible in possible_seq:
                            if possible in sequence_tracker:
                                    
                                    freq[possible] = sequence_tracker[possible]
                            else:
                                    
                                    sequence_tracker[possible] = 0
                                    freq[possible] = 0
                    if freq:
                            prediction = max(freq, key=freq.get)
                            print(f"Your most frequent sequence is {prediction}")
                            most_likely = prediction[-1]

                            if hint == "Y" or hint == "Yes":
                                 print(f" Hint: Mudabbir expects your sequence to end with '{most_likely}'.")
                                 print(f"He's getting ready to play '{ideal_response[most_likely]}'.")
                                 print("What's your counter move?")
                            else:
                                 print(f"Tracker: Mudabbir is tracking your recent sequence '{prediction}'.")
                                 print("He's targeting the final move of that pattern. Choose your counter.")
                            
                            print()
                    else:

                        print("Mudabbir is in random mode")
                        print()
                         
               
                else:
                     print("Mudabbir is in random mode")
                     print()


        
        
    while play not in ['R', 'P', 'S']:
        play = input("[R]ock, [P]aper, [S]cissors? ").upper()
        print(play)
        history.append(play)


    return play




'''
random player uses no stratergy to defeat opponent 
'''
def preeti(prev_opponent_play):

    return random.choice(['R', 'P', 'S'])



