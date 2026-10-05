import random
words = [("banking","it's associated with a place and people can work in said place as a profession: I am into _____"),
         ("letters", "You sent them mostly before phones were a thing, they are also related to the alphabet"),
         ("portfolio", "You have this when you are an artist, developer or designer"),
         ("landscape", "A type of picture or region of land"),
         ("earthquake", "A natural disaster"),
         ("Miami", "A city in South east florida")
         ]

# choose random word
# work function
def workflow(words):
    # Intro
    print("*" * 70)
    print()
    print(" Welcome to Jargon Jumble!")
    print(" A Tech-Themed Word Scramble Game")
    print()
    print("*" * 70)

    # Function to print game score
    def score_result(player_score):
        print("Game Decision: ",end = "")

        if(player_score == 5):
            print("Flawless, All tests passed. You're a natural!")
        elif(player_score == 4):
            print("Near perfect, you only failed one. Great effort!")
        elif(player_score == 3):
            print("Good effort, it's still halfway,so good work!")
        elif(player_score < 3):
            print("Dust yourself off and go again, there is always a way!")

    ALLOWED_ROUNDS = 5
    count = 1
    player_score = 0
    past_words = []

    # While loop to count rounds
    while count <= ALLOWED_ROUNDS:
        # Logic to make sure words aren't repeated
        chosen_word = random.choice(words)

        while chosen_word in past_words:
            chosen_word = random.choice(words)

        # change word to a list
        split_word = list(chosen_word[0])
        # print(split_word)

        # Shuffle elements in the list
        random.shuffle(split_word)
        # print(split_word)

        # Count from rounds 1 to 5
        print(f"Round {count} of {ALLOWED_ROUNDS}!")

        # Combine letters back to a string
        combined_word = "".join(split_word)
        print(f"Scrambled word: {combined_word.upper()}")

        user_guess = input("Enter your guess. Type 'skip' to skip the word"
                           " or 'hint to show a hint, 'quit' to quit the game: ")
        command = user_guess.lower().strip()
    # check if the user a hint or if they want to quit
        while command in ("hint","quit"):
            if command == 'hint':
                print(f"Your hint is {chosen_word[1]}")
                user_guess = input("Enter your guess. Type 'skip' to skip the word, 'hint' to show a hint, 'quit' to quit the game: ")
                command = user_guess.lower().strip()

            if command == 'quit':
                #Logic to confirm from user if they would like to quit
                print("Are you sure you want to quit this game? We will miss you")

                confirm = input("Enter Yes or No: ")

                if confirm.strip().lower() == 'yes':
                    print("Quitting Game 😣, Goodbye")
                    return

                else:
                    # if they do not quit,do not cost them a round.
                    user_guess = input(
                        "Enter your guess. Type 'skip' to skip the word, 'hint' to show a hint, 'quit' to quit the game: ")
                    command = user_guess.lower().strip()

    # Clean the guess
        cleaned_user_guess = command

    # conditional for logic
        if cleaned_user_guess == 'skip':
            print()
            print("No problem, we'll find another word.", "Your word was "+ chosen_word[0])
            print()
            # break while loop with no answer
            past_words.append(chosen_word)
            count+=1
            if count > ALLOWED_ROUNDS:
                print(f"You exceeded the available {ALLOWED_ROUNDS} rounds, Have a great day!")
                score_result(player_score)
            continue

        elif cleaned_user_guess != chosen_word[0].lower():
            print()
            print(f"Sorry, Your word was {chosen_word[0]}")

        else:
            print()
            print("Correct!✅ Keep Going")
            print()
            player_score += 1

        count+=1
        past_words.append(chosen_word)

        if count > ALLOWED_ROUNDS:
            print(f"You exceeded the available {ALLOWED_ROUNDS} rounds, Have a great day!")
            print()
            score_result(player_score)
            break

workflow(words)

