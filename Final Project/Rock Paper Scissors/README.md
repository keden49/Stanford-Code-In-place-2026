# Rock Paper Scissors

Welcome!

At its core, Rock, Paper, Scissors is a blind game. You never know what your opponent is about to play, and they never know what you are about to play. Every decision is made with incomplete information, winning is determined on the spot. This project builds on that idea by introducing opponents/bots that follow different strategies. Some are simple and predictable. Others adapt to your behavior and look for patterns in your move decisions.

Rules
- Enter R for Rock
- Enter P for Paper
- Enter S for Scissors

The standard rules apply:

- Rock beats Scissors
- Scissors beats Paper
- Paper beats Rock

Your the first player! Read about your opponents below and get familiar with how they work. Goodluck! I hope you enjoy the game.

---

## How to Play

1. Enable **Caps Lock**. The game only accepts uppercase inputs:
   - `R` for Rock
   - `P` for Paper
   - `S` for Scissors

2. Select an opponent.

3. Choose the number of rounds you would like to play.

4. Decide whether to enable hints. Hints explain how each algorithm makes decisions, while playing without them challenges you to uncover those strategies on your own.(I reccomend this option)
---

## Opponents

The algorithms are named after the professors, section leaders, and peers who contributed to my learning journey through Stanford's Code in Place.

### Preeti (Easy)

Plays completely at random.

There is no underlying strategy to uncover, making this the most unpredictable opponent despite being the simplest.

### Brahm (Easy)

Follows a repeating sequence of moves and ignores your actions entirely.

Success depends on identifying the pattern and anticipating the next move in the cycle.

**NB**: To understand Brahm stratergy play a minimal of 10 rounds

### Chris (Medium)

Chris always plays the counter to your last move

**Example**
```
Current Score {'Fathela': 2, 'chris': 0, 'tie': 0}

💡 Counters: R ➔ S | P ➔ R | S ➔ P (➔ = Beats)

Your Last move was P
To win you must counter the counter move to P which is S
[R]ock, [P]aper, [S]cissors? R
```

*In the example above, I chose to play **Rock** as Chris expects me to repeat **Paper**, so he will be  playing **Scissors** to counter it. Knowing this, I can counter his counter by playing **Rock**, which beats Scissors.*

### Mehran (Medium)

Tracks your recent moves and looks for the move you play most frequently and tries to counter it. If your habits become predictable, Mehran will quickly adapt to them.

**Example**

**Without Hint**

```
Current Score {'Fathela': 1, 'mehran': 0, 'tie': 0}

💡 Counters: R ➔ S | P ➔ R | S ➔ P (➔ = Beats)

Your most frequent move is currently R
To win you must counter Mehran's counter move to R

[R]ock, [P]aper, [S]cissors? S
```

**With Hint**

```
Current Score {'Fathela': 1, 'mehran': 0, 'tie': 0}

💡 Counters: R ➔ S | P ➔ R | S ➔ P (➔ = Beats)

Shhh ... 🤫 This is a secret hint
Mehran expects you to play R next
To win you must counter his own counter move which is P

[R]ock, [P]aper, [S]cissors? S
```


*In both examples, I chose **Scissors**. Mehran's strategy is to identify my most frequent move, which is currently **Rock**, and play its counter, **Paper**. Knowing this, I can anticipate his move and play **Scissors**, which beats Paper.*



### Juliette (Hard)

Tracks combinations of consecutive moves, and keeps their count, and uses those patterns to predict what you are likely to play next. The more consistent your behavior becomes, the more accurate her predictions become.

**Example**

**Without Hint**


```
Current Score {'Fathela': 1, 'juliette': 0, 'tie': 0}

💡 Counters: R ➔ S | P ➔ R | S ➔ P (➔ = Beats)

Your most frequent pair of moves is SR
Tracker: Juliette noticed your frequent pair 'SR'.
She's preparing her next move based on the end of that sequence. Choose wisely.

[R]ock, [P]aper, [S]cissors? S
```

**With Hint**

```
Current Score {'Fathela': 1, 'juliette': 0, 'tie': 0}

💡 Counters: R ➔ S | P ➔ R | S ➔ P (➔ = Beats)

Your most frequent pair of moves is SR
Hint: Juliette predicts you will play 'R'.
She's planning to play 'P' to beat it.
What will you play to counter her?

[R]ock, [P]aper, [S]cissors? S
```

*In both examples, I chose **Scissors**. Juliette analyzes pairs of consecutive moves and uses them to predict what I am likely to play next. In this case, the pair **SR** appears most frequently in my history, leading her to predict that my next move will be **Rock**. To counter that prediction, she plans to play **Paper**. Knowing this, I can anticipate her response and play **Scissors**, which beats Paper.*


### Mudabbir (Expert)

A custom algorithm based on a four-step Markov chain.

Rather than focusing on individual moves, Mudabbir analyzes longer sequences and searches for recurring patterns in your play history. The opening rounds are used to collect information before predictions begin.

**Example**

**Random Mode**

```
Current Score {'Fathela': 1, 'mudabbir': 1, 'tie': 2}

💡 Counters: R ➔ S | P ➔ R | S ➔ P (➔ = Beats)

Your most frequent sequence is SRSR
Hint: Mudabbir expects your sequence to end with 'R'.
He's getting ready to play 'P'.
What's your counter move?

[R]ock, [P]aper, [S]cissors? S
```

*When Mudabbir is in random mode it means, the number of rounds played are not enough for the bot to form coherent algorithms for it to base its predictions. Hence it plays random moves*

**Without Hint**

```
Current Score {'Fathela': 2, 'mudabbir': 0, 'tie': 1}

💡 Counters: R ➔ S | P ➔ R | S ➔ P (➔ = Beats)

Your most frequent sequence is SPRR
Tracker: Mudabbir is tracking your recent sequence 'SPRR'.
He's targeting the final move of that pattern. Choose your counter.

[R]ock, [P]aper, [S]cissors? S

```


**With Hint**

```
Current Score {'Fathela': 1, 'mudabbir': 1, 'tie': 2}

💡 Counters: R ➔ S | P ➔ R | S ➔ P (➔ = Beats)

Your most frequent sequence is SRSR
Hint: Mudabbir expects your sequence to end with 'R'.
He's getting ready to play 'P'.
What's your counter move?

[R]ock, [P]aper, [S]cissors? S


**NB**: To understand Mudabbir's stratergy play a minimal of 20 rounds
```

*In both examples, I chose **Scissors**. Mudabbir tracks recurring sequences of four moves and learns which moves tend to follow them. In the first example, the sequence **SPRR** appears frequently in my history. Since the sequence ends with **Rock**, Mudabbir expects Rock to be the most likely outcome and prepares **Paper** to counter it. Anticipating this, I play **Scissors**, which beats Paper.*

**Note**: For the best experience, play at least 20 rounds to allow meaningful patterns to emerge.



---

## Understanding the Hints

The game includes an optional hint system that reveals what information an algorithm is currently using to make decisions.

If hints are disabled, the terminal provides only the raw data available to the algorithm, leaving it up to you to interpret what it means.

### Example

```text
Current Score {'Player': 2, 'mudabbir': 0, 'tie': 1}

Counters: R -> S | P -> R | S -> P

Tracker: Mudabbir is tracking your recent sequence 'RRPR'.
He's targeting the final move of that pattern.

[R]ock, [P]aper, [S]cissors?
```

In this example, the algorithm has identified a sequence in your recent history and is using it to predict your next move. The challenge is to determine what it expects and respond accordingly.

---

## Closing Thoughts

This project is ultimately less about Rock, Paper, Scissors and more about patterns.
Every algorithm in this game follows a set of rules. Some are obvious, some are subtle, and some require a bit of experimentation to uncover. Winning consistently comes from understanding those rules and adapting your decisions around them.

The same idea appears throughout machine learning, where models learn from patterns in data and make predictions based on what they have observed before.

This project simply turns that process into a game.

## Running The Game 

### Prerequisites

Before running the game, make sure you have:

- Python 3 installed
- Visual Studio Code (recommended)


### Step 1: Download the Repository

Clone the repository:

```bash
git clone https://github.com/keden49/Stanford-Code-In-place-2026.git
```

Or:

1. Click the green **Code** button.
2. Select **Download ZIP**.
3. Extract the ZIP file.

### Step 2: Open the Repository

Open the downloaded repository in Visual Studio Code.

### Step 3: Navigate to the Project

In the VS Code file explorer, open:

```text
Final Project/
└── Rock Paper Scissors/
    └── main.py
```

### Step 4: Run the Game

Open `main.py` and click the **Run Python File** button (▶) in the top-right corner of VS Code.

Alternatively:

1. Right-click anywhere inside `main.py`.
2. Select **Run Python File in Terminal**.

The game will start automatically.


### Why Run It This Way?

The project is organized into multiple Python files that import functionality from one another. Running the game from the repository root ensures that all modules can be located correctly.

