Jargon Jumble
Jargon Jumble is a Python command-line word scramble game where players try to identify randomly shuffled words across multiple rounds.
The project was created as part of my Python learning process to practice functions, loops, conditionals, lists, tuples, randomization, string manipulation, user input, and basic game-state management.
Features
- Randomly selects words from a word bank
- Scrambles the letters before each round
- Runs for up to 5 rounds
- Prevents previously used words from repeating
- Allows players to request hints
- Allows players to skip a word
- Includes a quit confirmation flow
- Tracks the player's score
- Displays a final message based on the player's result
- Normalizes user input with .strip() and .lower()
Example
**********************************************************************

 Welcome to Jargon Jumble!
 A Tech-Themed Word Scramble Game

**********************************************************************

Round 1 of 5!
Scrambled word: OTIRFLOOP

Enter your guess.
Type 'skip' to skip the word, 'hint' to show a hint, or 'quit' to quit the game:

portfolio

Correct!✅ Keep Going

Word Bank
The current game includes words such as:
- banking
- letters
- portfolio
- landscape
- earthquake
- Miami
Each word is stored with a corresponding hint.

Example:
("portfolio", "You have this when you are an artist, developer or designer")
Technologies
- Python
- Python random module
Concepts Practiced
This project helped reinforce several Python fundamentals i am an expert in:
- Variables
- Lists
- Tuples
- Functions
- Nested functions
- while loops
- Nested loops
- if, elif, and else
- break
- continue
- return
- String manipulation
- .lower()
- .strip()
- .join()
- List conversion
- Membership checks with in
- Random selection with random.choice()
- Random shuffling with random.shuffle()
- Score tracking
- Round tracking
- Preventing duplicate selections
- Basic command handling
- 
Game Flow
1. The game starts with a welcome message.
2. A random word is selected from the word bank.
3. The letters are shuffled and displayed to the player.
4. The player can:
   - Enter a guess
   - Type hint to view a clue
   - Type skip to move to another word
   - Type quit to leave the game
5. Correct answers increase the player's score.
6. Previously used words are stored so they are not selected again.
7. After 5 rounds, the game displays the player's final result.
Scoring
The game currently evaluates the final score as follows:
Score	Result
5/5	Flawless — all tests passed
4/5	Near perfect
3/5	Good effort
0–2/5	Encouragement to try again

Project Structure
jargon-jumble/
├── jargon_jumble.py
└── README.md
Running the Project
1. Clone the repository
git clone <your-repository-url>
2. Move into the project folder
cd jargon-jumble
3. Run the game
python jargon_jumble.py

Possible improvements include:
- Add a larger word bank
- Add difficulty levels
- Add categories
- Prevent a shuffled word from matching the original word
- Add replay functionality
- Add a high-score system
- Save scores to a file
- Add multiple hints per word
- Add limited hint usage
- Add better input validation
- Separate game logic into additional reusable functions
- Move the word bank into an external file
- Add automated tests
- Build a graphical or web-based version

Purpose
Jargon Jumble started as a Python practice exercise and developed into a small interactive command-line game.
The goal was to move beyond isolated syntax exercises and combine multiple Python concepts into one working program with user interaction, state tracking, scoring, randomization, and game-flow logic.
Author
Supreme Emhenya
- GitHub: Emya101
- LinkedIn: Supreme Emhenya
