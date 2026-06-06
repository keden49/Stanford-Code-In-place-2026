# RPS: Beat Them At Their Own Game
## Project Description 

This project was inspired by the Rock Paper scissors challenge by freecodecamp which was one of my final projects in the Machine Learning with Python Curriculum. In this original project, the objective was to develop a Rock, Paper, Scissors program capable of competing against multiple predefined algorithms. To successfully complete the challenge, the program needed to achieve a win rate of at least 60% against each of four different opponent algorithms.


I took that idea and decided to create an extra bot algorithm which uses a more sophisticated stratergy to defeat its opponents while also giving others the prvildege to interact with the original algorithms. 

In this project the algorithm uses a 4 window Markov chain to counter an opponent, this algorithm takes into assumption that humans are very repetitive and thus predictable. it Keeps count of last 4 moves and makes a prediction based on the dequence the opponent likes to take ......

At the end of the program the user is given their own play patterns and opponets history to understand the players logic 


# Keep in mind the players Algorithm doesn't change what changes is you .....

The user should be asked how many number of games they wish to play
the game should dispalay the champion with a trophy 
if player loses ther is an encouragement message 
the algorithms including mine should have proffesors names
my final algorithm should have my section leader name for he was smart
explain the rules to players regarding how to play 
instruct palyers to have caps lock on 
explain in agame o rps you never see opponets stratergy rather know what they are going to play 
its a blind game 
but you can always study opponets moves 
and understand their stratergy 
provide a list where players can choose opponets and call the neccesary opponent 
dont make the game tooo complicated
Add current score board 
As the game progresses

Are you confident in your Rock Paper Scissors skills ?
You can put them to the test by playing against different bots who use different strategies defat you

Introducing the bots 

I decided to name the bots after professors and section leaders and mates  who took us through code in place to make the lessons more palatable/ familiar 

1. Chris - always counters your last move eg 
...
2. Mehran - always counters you with your most frequent move from your last 10 rounds 
3. Brahm - uses a repeating sequence and never changes 
4. Juliette - very smart, keeps count of your moves in pairs and makes a prediction based on the most frequent
5. Mudabbir - like juliette, mudabbir also keeps count but in groups of keeps count of every possible combination of moves - hardest bot to beat 

6. Preeti - random stratergy , should be the easist bot to beat though, she can win through luck 


To discover patterns and uncover players stratergy you can always check opponents history which contain past moves studying them gives you time to predict next move

To understand Juliette one must analyze her move tracker and counter her by checking whats most frequent and countering the last move for 
example 

note that when all possible next moves have the same frequency it always counters "R" meaning it plays "P"

if Juliette You will be given their current tracker 
analyze what you played last , find out all posibilities your last move could take which is 
move plus each possible move 
meaning if it is P 
possible next moves are PR, PP, PS and if R RR,RP,RS and if S SR,SS,SP

look at your most frequent pair. Juliette will ost likely be countering that. So for you to effectively counter Juliette You must counter the counter of juliette 

The same applies to mahren

To win this game you must think like your player 
you must embody the mind of the player 


For mehran you will be given your most frequent move it will be up to you to figure out the most appropriate counter

for brahm look for a sequence of repeating patterns do you notice one 


To counter Muddabir 


when Mudabbir is in random mode it means he hasnt formed any coherent sequence to understnad how you play in this case Mudabbir plays Randomly without any stratergy in order to figure you out 

after four rounds coherent patterns will start forming 

To play effectively put caps lock on 

Minimum Number of games


This game utilizes dictionaries, lists decomposition of functions ...manipulation of variables 

The game is blind so you you never know what they are about to play but the only thing you know is their stratergy
you can optionally choose to have hint

in project description caution the user to read the readme first to familiarize with the opponents and how the game goes 

talk about inspirations of the project 