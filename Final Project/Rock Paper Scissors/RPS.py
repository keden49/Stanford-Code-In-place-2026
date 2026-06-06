import random

moves = ["R","P","S"]

# keeps count of unique move sequences from opponent 

user_seq  = {}
n_grams = 3

'''
An algorithm that uses Markov Chain 
a probabilistic model used to predict an opponent's next move 
based entirely on their previous actions.
'''
def mudabbir(prev_play, opponent_history = []):
        
        global moves, user_seq,n_grams
        # all moves and their counter moves 

        ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

        # avoids empty string characters 
        if not prev_play:
                prev_play = "R"
       
        opponent_history.append(prev_play)

        # cleans up memory when new game begins 
        if len(opponent_history) == 1000:
                opponent_history.clear()
                user_seq.clear()

        if len(opponent_history) > n_grams:
                
                # current sequence 

                seq ="".join(opponent_history[-(n_grams):])

                # last sequence 

                last_seq = "".join(opponent_history[-(n_grams + 1):])
                
                # add new play sequence

                if last_seq not in user_seq:
                        user_seq[last_seq] = 1
                
                # add count if already exists 

                else:
                        user_seq[last_seq] += 1

                
                # possible next sequences 

                possible_seq = [seq + move for move in moves]
                
                # get possible sequences and their count 
                freq = {}
                for possible in possible_seq:
                        
                        if possible in user_seq:
                                
                                freq[possible] = user_seq[possible] # get count
                        else:
                                # if the sequences dont exist add them in the user seq
                                user_seq[possible] = 0
                                freq[possible] = 0

                
                # gets the most frequent seq
                # identifies the last element as the opponents estimated next move
                # along as freq is non emty
                if freq:
                        prediction = max(freq, key = freq.get)[-1] # get the very last element

                        # counter opponent based on their most likely next move

                        counter = ideal_response[prediction]

                        return counter
                
                # if freq is empty return random moves
                else:
                        
                        return random.choice(moves)
                        
        
        else: 
               # play random moves if there is not enough data to form sequences
               return random.choice(moves)
                

            




    
       
    



